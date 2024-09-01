# Bot de Atendimento para Estabelecimentos Gerais

O projeto é um bot de pré-atendimento desenvolvido usando Python, Flask e Twilio. O bot é projetado para responder automaticamente a mensagens recebidas via WhatsApp, fornecendo informações úteis e registrando interações em um banco de dados SQLite. Ele é adaptável para diferentes tipos de estabelecimentos, como lojas, restaurantes, e serviços.

## 🔨 Funcionalidades do Projeto

- **Recepção de Mensagens:** O bot recebe mensagens enviadas para o número do WhatsApp configurado.
- **Resposta Automática:** O bot responde com informações relevantes baseadas em palavras-chave nas mensagens recebidas.
- **Registro de Mensagens:** Registra cada mensagem recebida e a resposta enviada em um banco de dados SQLite.
- **Integração com Twilio:** Utiliza a API do Twilio para enviar e receber mensagens via WhatsApp.

### Exemplo Visual do Projeto

O projeto é um serviço backend e não possui uma interface visual. No entanto, o bot pode interagir com o usuário via mensagens no WhatsApp.

## ✔️ Técnicas e Tecnologias Utilizadas

- **Python:** Linguagem de programação utilizada para o desenvolvimento do bot.
- **Flask:** Framework web para criar o servidor e gerenciar as requisições.
- **Twilio:** Serviço de comunicação utilizado para enviar e receber mensagens via WhatsApp.
- **SQLite:** Banco de dados leve utilizado para registrar mensagens e respostas.

## 📁 Estrutura do Projeto

- **app.py:** Código principal do bot que lida com requisições, respostas e registro de mensagens.
- **LICENSE:** Arquivo de licença do projeto.
- **README.md:** Documento de documentação do projeto.
- **requirements.txt:** Lista de dependências do projeto.
- **static/**: Diretório para arquivos estáticos (não utilizado neste projeto, pode ser removido ou usado no futuro).
- **templates/**: Diretório para arquivos de template (não utilizado neste projeto, pode ser removido ou usado no futuro).

## 🛠️ Abrir e Rodar o Projeto

Para iniciar o projeto localmente, siga os passos abaixo:

1. **Certifique-se de que o Python está instalado**:
    - O [Python](https://www.python.org/) é necessário para rodar o projeto. Você pode verificar se já o tem instalado com:
      ```bash
      python --version
      ```
    - Se não estiver instalado, baixe e instale a versão recomendada.

2. **Clone o Repositório**:
    - Copie a URL do repositório e execute o comando abaixo no terminal:
      ```bash
      git clone <URL_DO_REPOSITORIO>
      ```
    - Navegue até o diretório do projeto:
      ```bash
      cd <NOME_DO_REPOSITORIO>
      ```

3. **Instale as Dependências**:
    - Utilize o arquivo `requirements.txt` para instalar todas as dependências necessárias:
      ```bash
      pip install -r requirements.txt
      ```

4. **Configure as Variáveis de Ambiente**:
    - Configure as variáveis de ambiente do Twilio diretamente no código ou no ambiente de desenvolvimento. As variáveis necessárias são:
        - `TWILIO_SID`
        - `TWILIO_AUTH_TOKEN`
        - `TWILIO_PHONE_NUMBER`

5. **Inicie o Servidor Flask**:
    - Execute o script `app.py` para iniciar o servidor Flask:
      ```bash
      python app.py
      ```

    - Certifique-se de que o servidor está rodando e acessível pela URL configurada no Twilio para o webhook.

## 🌐 Deploy

Para um ambiente de produção, considere hospedar o projeto em um serviço de hospedagem como Heroku, AWS, ou Google Cloud. Certifique-se de configurar variáveis de ambiente e webhooks conforme necessário.

