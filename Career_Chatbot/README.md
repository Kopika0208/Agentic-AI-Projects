# Career Conversation Chatbot

An AI-powered professional representative that answers queries on Kopika's portfolio website. It uses her resume, profile, and summary to generate human-like responses and simulate authentic conversations with potential clients or employers.

## Features

- Extracts and processes resume and profile PDFs
- Uses a structured background summary for context
- Persona-based system prompt to mimic M Kopika
- Answers professionally and suggests email follow-up when needed
- Built with Gradio interface for easy interaction

## Tech Stack

- Python 3.12
- Google Gemini (via OpenAI-compatible interface) for dialogue generation
- `pypdf` for PDF extraction
- `Gradio` for building a web chat interface
- `.env` for secure API key handling

## How It Works

1. Resume pdf and Profile pdf files are parsed using `pypdf`.
2. The system combines extracted text with a manually written `summary.txt` file.
3. A long system prompt is constructed to guide the chatbot to roleplay as M Kopika.
4. All user queries and system instructions are passed to Gemini via a chat API call.
5. The chatbot responds in M Kopika's tone, offering relevant, context-aware answers.
6. For questions it can't handle, the agent recommends contacting Kopika via email.
7. The conversation is deployed using Gradio’s chat interface for real-time interaction.
