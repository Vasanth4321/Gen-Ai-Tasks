# Blog Assistant Chatbot

A Streamlit-based Blog Assistant Chatbot powered by Google's Gemini AI.

The application helps users generate blog ideas, create outlines, improve content quality, and receive SEO-friendly writing suggestions through a conversational interface.

## Features

* AI-powered blog writing assistance
* Google Gemini API integration
* Secure API key management using environment variables
* Modular API implementation
* Session-based conversation history
* Real-time response generation
* Chat-style user interface
* Download individual responses as Markdown files
* Download complete conversation history as a Markdown file
* Logging and exception handling

## Project Structure

```text
Task2/
│
├── app.py
├── gemini_client.py
├── requirements.txt
├── README.md
└── .env
```

## Installation

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

## Running the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## Usage

1. Enter a blogging-related question.
2. Receive AI-generated guidance or content.
3. Download individual responses as Markdown files.
4. Download the complete conversation from the sidebar.
5. Clear the chat history when required.

## Technologies Used

* Python
* Streamlit
* Google Gemini API (`google-genai`)
* python-dotenv

## Future Improvements

* Blog export as markdown
* Conversation persistence using a database
* Multiple AI personas
* SEO scoring and keyword analysis
* Blog template generation

## Author

Developed as part of a Generative AI assignment/project.
