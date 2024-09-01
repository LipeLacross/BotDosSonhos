# Customer Service Bot for General Establishments

The project is a pre-service bot developed using Python, Flask, and Twilio. The bot is designed to automatically respond to messages received via WhatsApp, providing useful information and recording interactions in an SQLite database. It is adaptable to different types of establishments, such as stores, restaurants, and services.

## 🔨 Project Features

- **Message Reception:** The bot receives messages sent to the configured WhatsApp number.
- **Automatic Response:** The bot responds with relevant information based on keywords in the received messages.
- **Message Logging:** Logs each received message and the response sent in an SQLite database.
- **Integration with Twilio:** Uses the Twilio API to send and receive messages via WhatsApp.

### Visual Example of the Project

The project is a backend service and does not have a visual interface. However, the bot can interact with users via WhatsApp messages.

## ✔️ Techniques and Technologies Used

- **Python:** Programming language used for bot development.
- **Flask:** Web framework for creating the server and managing requests.
- **Twilio:** Communication service used for sending and receiving messages via WhatsApp.
- **SQLite:** Lightweight database used for logging messages and responses.

## 📁 Project Structure

- **app.py:** Main bot code that handles requests, responses, and message logging.
- **LICENSE:** Project license file.
- **README.md:** Project documentation file.
- **requirements.txt:** List of project dependencies.
- **static/**: Directory for static files (not used in this project, can be removed or used in the future).
- **templates/**: Directory for template files (not used in this project, can be removed or used in the future).

## 🛠️ Running the Project

To run the project locally, follow these steps:

1. **Ensure Python is Installed**:
    - [Python](https://www.python.org/) is required to run the project. You can check if it's already installed with:
      ```bash
      python --version
      ```
    - If not installed, download and install the recommended version.

2. **Clone the Repository**:
    - Copy the repository URL and run the following command in the terminal:
      ```bash
      git clone <REPOSITORY_URL>
      ```
    - Navigate to the project directory:
      ```bash
      cd <REPOSITORY_NAME>
      ```

3. **Install Dependencies**:
    - Use the `requirements.txt` file to install all necessary dependencies:
      ```bash
      pip install -r requirements.txt
      ```

4. **Configure Environment Variables**:
    - Configure the Twilio environment variables directly in the code or development environment. The required variables are:
        - `TWILIO_SID`
        - `TWILIO_AUTH_TOKEN`
        - `TWILIO_PHONE_NUMBER`

5. **Start the Flask Server**:
    - Run the `app.py` script to start the Flask server:
      ```bash
      python app.py
      ```

    - Ensure the server is running and accessible via the URL configured in Twilio for the webhook.

## 🌐 Deploy

For a production environment, consider hosting the project on a hosting service such as Heroku, AWS, or Google Cloud. Be sure to configure environment variables and webhooks as needed.
