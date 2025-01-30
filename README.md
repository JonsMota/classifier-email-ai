#  Classifier Email AI

## Descrição

Esta aplicação web utiliza inteligência artificial para classificar emails em categorias predefinidas (Produtivo e Improdutivo) e sugerir respostas automáticas baseadas na classificação realizada. O objetivo é automatizar a leitura e classificação de emails, liberando tempo da equipe para outras tarefas.

## Estrutura do Projeto

AUTOU-DESAFIO/
├── static/
│   └── style.css
├── backend/
│   └── classifier.py
│   └── app.py
├── frontend/
│   └── index.html
│   └── result.html
├── .env
├── .gitignore
├── README.md
├── requirements.txt


## Pré-requisitos

- Python 3.7 ou superior
- Conta no OpenAI com chave de API
- Conta no GitHub
- Conta na Vercel (opcional, para hospedagem)

## Configuração do Ambiente

1. Clone o Repositório:

   ```sh
   git clone https://github.com/JonsMota/classifier-email-ai.git
   cd email-classifier-ai
   ```
2. Crie um Ambiente Virtual:

    ```sh
    python -m venv venv
    ```
3. Ative o ambiente virtual:  

    No Windows:
    ```sh
    venv\Scripts\activate
    ```
    No Unix ou MacOS:
    ```sh
    source venv/bin/activate
    ```

4. Instale as Dependências:

    ```sh
    pip install -r requirements.txt
    ```

5. Configure a Key da API do OpenAI:

    Acesse OpenAI e crie uma conta. 

    Após criar a conta, vá para a seção de API Keys e gere uma nova chave de API.

    Crie um arquivo [.env](http://_vscodecontentref_/1) na raiz do projeto e adicione sua chave de API do OpenAI:
        ```env
    API_KEY=your_openai_api_key
        ```

5. **Baixe os Recursos do NLTK:**

    No terminal Python, execute:

    ```python
    import nltk
    nltk.download('stopwords')
    nltk.download('punkt')
    ```

Executando a Aplicação Localmente
Inicie o Servidor Flask:

Acesse a Aplicação:

Abra o navegador e vá para http://127.0.0.1:5000.

Hospedagem na Vercel
Crie um Repositório no GitHub:

Acesse github.com e crie um novo repositório.
Clone o repositório e copie os arquivos do projeto para o diretório clonado.
Adicione, faça commit e envie os arquivos para o GitHub.
Hospede na Vercel:

Acesse vercel.com e faça login.
Clique em "New Project" e selecione "Import Git Repository".
Conecte sua conta do GitHub e selecione o repositório classifier-email-ai.
Clique em "Import" e siga as instruções para configurar o projeto.
Adicione a variável de ambiente API_KEY com a chave da API do OpenAI no painel de configurações do projeto na Vercel.
Clique em "Deploy".

Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Desenvolvido por Jonas com 💻 e ☕.


### Conclusão

O arquivo `README.md` deve ser colocado na pasta raiz do seu projeto (`AUTOU-DESAFIO/`). Ele fornece instruções claras sobre como configurar e executar a aplicação localmente, além de informações sobre a estrutura do projeto, pré-requisitos, e como hospedar a aplicação na Vercel.
### Conclusão

O arquivo `README.md` deve ser colocado na pasta raiz do seu projeto (`AUTOU-DESAFIO/`). Ele fornece instruções claras sobre como configurar e executar a aplicação localmente, além de informações sobre a estrutura do projeto, pré-requisitos, e como hospedar a aplicação na Vercel.

### Respostas:

1. ***Dependências no `requirements.txt` para evitar erros na Vercel:**
   Certifique-se de que todas as dependências necessárias estão listadas no `requirements.txt`.

2. **Instale as dependências:**

   ```plaintext
   flask
   transformers
   torch
   pdfminer.six
   nltk
   openai
   python-dotenv
   ```

3. **Configurar variáveis de ambiente na Vercel:**
   - Acesse o painel da Vercel.
   - Selecione o projeto.
   - Vá para "Settings" > "Environment Variables".
   - Adicione a variável `API_KEY` com o valor da sua chave de API do OpenAI.
   - Clique em "Add".

4. **Arquivo .gitignore**

    ```plaintext
    # Ignore environment variables
    .env

    # Ignore Python cache files
    __pycache__/
    *.py[cod]

    # Ignore system files
    .DS_Store
    Thumbs.db

    # Ignore virtual environment
    venv/
    ```

5. **Sequência de comandos para GitHub:**

   ```sh
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/JonsMota/classifier-email-ai.git
   git push -u origin main
   ```

6. **Hospedagem na Vercel:**

   - **Passo 1:** Crie um repositório no GitHub e faça o push do seu projeto.
   - **Passo 2:** Acesse [vercel.com](https://vercel.com) e faça login.
   - **Passo 3:** Clique em "New Project" e selecione "Import Git Repository".
   - **Passo 4:** Conecte sua conta do GitHub e selecione o repositório `email-classifier-ai`.
   - **Passo 5:** Clique em "Import" e siga as instruções para configurar o projeto.
   - **Passo 6:** Adicione a variável de ambiente `API_KEY` no painel de configurações do projeto na Vercel.
   - **Passo 7:** Clique em "Deploy".

