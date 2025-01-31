import openai
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from openai.error import RateLimitError, OpenAIError
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do .env
load_dotenv()
openai.api_key = os.getenv('API_KEY')

def preprocess_email(content):
    stop_words = set(stopwords.words('portuguese'))
    words = word_tokenize(content)
    return ' '.join([word for word in words if word.lower() not in stop_words])

def classify_email(content):
    prompt = (
        "Classifique o seguinte email como 'Produtivo' ou 'Improdutivo'. "
        f"Aqui está o email: {content}"
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        classification = response['choices'][0]['message']['content'].strip()
        return classification
    except RateLimitError:
        return "Rate limit exceeded. Please try again later."
    except OpenAIError as e:
        return f"Erro: {str(e)}"

def generate_response(category, content):
    prompt = f"O email abaixo foi classificado como {category}. Gere uma resposta apropriada: {content}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except RateLimitError:
        return "Rate limit exceeded. Please try again later."
    except OpenAIError as e:
        return f"Erro: {str(e)}"