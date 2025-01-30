import openai
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from openai.error import RateLimitError
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()
# Defina sua chave de API aqui
openai.api_key = os.getenv('API_KEY')

def preprocess_email(content):
    stop_words = set(stopwords.words('portuguese'))
    words = word_tokenize(content)
    return ' '.join([word for word in words if word.lower() not in stop_words])

def classify_email(content):
    prompt = (
        "Você é um assistente útil. Classifique o seguinte email como 'Produtivo' ou 'Improdutivo'. "
        "Um email produtivo contém informações relevantes, claras e importantes para o trabalho. "
        "Um email improdutivo não contém informações úteis ou é irrelevante para o trabalho. "
        f"Aqui está o email: {content}"
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": prompt}
            ]
        )
        classification = response['choices'][0]['message']['content'].strip()
        return classification
    except RateLimitError:
        return "Rate limit exceeded. Please try again later."
    except OpenAIError as e:
        return f"An error occurred: {str(e)}"

def generate_response(category, content):
    if category == "Produtivo":
        prompt = f"O email abaixo foi classificado como {category}. Gere uma resposta profissional para este conteúdo: {content}"
    else:
        prompt = f"O email abaixo foi classificado como {category}. Responda educadamente que nenhuma ação é necessária."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except RateLimitError:
        return "Rate limit exceeded. Please try again later."
    except OpenAIError as e:
        return f"An error occurred: {str(e)}"