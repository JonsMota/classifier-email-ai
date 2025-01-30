import sys
import os
import nltk
from flask import Flask, request, render_template
from classifier import preprocess_email, classify_email, generate_response  # Importa diretamente de 'classifier'
from openai.error import RateLimitError

# Baixar os recursos 'stopwords' e 'punkt' do NLTK
nltk.download('stopwords')
nltk.download('punkt')

sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))  # Adiciona o diretório 'backend' ao caminho de importação

app = Flask(__name__, template_folder='../frontend', static_folder='../static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    content = None
    for encoding in ['utf-8', 'latin1', 'cp1252']:
        try:
            content = file.read().decode(encoding)
            break
        except UnicodeDecodeError:
            continue
    if content is None:
        return "Failed to decode file", 400

    preprocessed_content = preprocess_email(content)
    category = classify_email(preprocessed_content)
    try:
        response = generate_response(category, content)
    except RateLimitError:
        return "Rate limit exceeded. Please try again later.", 429

    return render_template('result.html', category=category, response=response)

if __name__ == '__main__':
    app.run(debug=True)