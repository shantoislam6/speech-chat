# Speech Recognition and Text-to-Speech Application

## Overview

This Python application leverages speech recognition and text-to-speech technologies to interact with users through voice commands. It uses OpenAI's GPT-3.5-turbo (or GPT-4) model to generate responses to user queries.

## Requirements

- Python 3.x
- `speech_recognition` for recognizing speech
- `pyttsx3` for text-to-speech functionality
- `openai` for interfacing with the OpenAI API
- `python-dotenv` for managing environment variables

## Setup

1. **Install Dependencies:**

   ```bash
   pip install speech_recognition pyttsx3 openai python-dotenv
   ```
2. **Create a `.env` File:**

   Ensure you have a `.env` file in the same directory as your script with the following content:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```
