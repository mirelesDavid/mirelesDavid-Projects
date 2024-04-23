# Voice Assistant with OpenAI Integration

This project is a voice assistant built with Python that integrates with OpenAI's GPT-3 language model. The assistant can perform various tasks such as playing music, opening websites, providing the current date and time, searching Wikipedia, and answering general queries using OpenAI's natural language processing capabilities.

## Features

- Speech recognition for voice commands
- Text-to-speech for audible responses
- Integration with OpenAI's GPT-3 language model for natural language processing
- Play music from YouTube
- Open websites in the default browser
- Get the current date and time
- Search Wikipedia for information
- General query handling using OpenAI's language model

## Technologies Used

- Python
- SpeechRecognition (for speech recognition)
- pyttsx3 (for text-to-speech)
- openai (for integrating with OpenAI's GPT-3 API)
- webbrowser (for opening URLs in the default browser)
- pywhatkit (for playing music from YouTube)
- wikipedia (for searching Wikipedia)

## Prerequisites

Before running the project, make sure to have the following prerequisites installed:

- Python (version 3.6 or later)
- Required Python packages: `SpeechRecognition`, `pyttsx3`, `openai`, `webbrowser`, `pywhatkit`, `wikipedia`

You can install the required packages using pip:

Additionally, you need to obtain an API key from OpenAI and replace the placeholder in the code with your actual API key.

## Usage

1. Clone or download the project files.
2. Open the project directory in your terminal or command prompt.
3. Replace the placeholder `"sk-YOUR_API_KEY"` with your actual OpenAI API key.
4. Run the `voice_assistant.py` file:
5. The assistant will greet you and start listening for voice commands.
6. Use the activation word "charles" followed by your command (e.g., "charles open google.com", "charles play music", "charles what is the time?", "charles please tell me about the solar system").
7. The assistant will process your command and provide the appropriate response through text-to-speech.
8. To exit the assistant, say "charles kill" or press Ctrl+C.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
