# AI-Powered Knowledge Assistant

An AI-powered conversational assistant built with Python and the Groq API.

The application provides a normal conversational mode and allows users to switch between specialized assistant roles such as HR Assistant, Python Trainer, AI Interviewer, and Software Architect.

It also includes conversation history, retry handling, API error handling, prompt validation, and application logging.

---

## Features

- Normal AI assistant mode
- Role-based assistant modes
- Dynamic role switching
- HR Assistant
- Python Trainer
- AI Interviewer
- Software Architect
- Conversation history
- Last 10 messages maintained in conversation history
- API retry mechanism
- API timeout handling
- Network error handling
- Missing API key handling
- Empty prompt validation
- Long prompt validation
- Keyboard interrupt handling
- Response time logging
- `.env` based configuration

---

## Assistant Roles

The application supports four specialized roles.

### 1. HR Assistant

Provides professional assistance for HR-related questions and topics.

### 2. Python Trainer

Explains Python concepts using simple explanations and practical examples.

### 3. AI Interviewer

Acts as a technical interviewer, asks interview questions, evaluates answers, and provides feedback.

### 4. Software Architect

Provides guidance related to software architecture, system design, APIs, databases, scalability, and design decisions.

---

## Project Structure

```text
AI-Assistant/
│
├── app.py                  # Main application
├── chatbot.py              # Chatbot and LLM interaction
├── config.py               # Environment configuration
├── prompts.py              # Role-based prompt templates
├── logger.py               # Logging configuration
├── utils.py                # Utility functions
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Git ignored files
├── .env                    # Environment variables (not committed)
│
├── logs/
│   └── assistant.log      # Application logs
│
└── venv/                   # Python virtual environment
