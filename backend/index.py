import os
import nltk
from flask import Flask, request, render_template
from backend.classifier import preprocess_email, classify_email, generate_response
from openai.error import RateLimitError

# Baixar os recursos necessários do NLTK
nltk.download('stopwords')
nltk.download('punkt')

# Configuração do Flask
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
        return "Falha ao decodificar arquivo", 400

    preprocessed_content = preprocess_email(content)
    category = classify_email(preprocessed_content)
    try:
        response = generate_response(category, content)
    except RateLimitError:
        return "Limite de requisições excedido. Tente novamente mais tarde.", 429

    return render_template('result.html', category=category, response=response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))