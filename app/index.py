import os
from classifier import preprocess_email, classify_email, generate_response
from flask import Flask, request, render_template
from openai.error import RateLimitError

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "Nenhum arquivo enviado", 400
    file = request.files['file']
    if file.filename == '':
        return "Nenhum arquivo selecionado", 400
    content = file.read().decode('utf-8')  # Lê o conteúdo do arquivo

    preprocessed_content = preprocess_email(content)
    category = classify_email(preprocessed_content)
    try:
        response = generate_response(category, content)
    except RateLimitError:
        return "Limite de requisições excedido. Tente novamente mais tarde.", 429

    return render_template('result.html', category=category, response=response)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)