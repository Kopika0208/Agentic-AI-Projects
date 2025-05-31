# Sales Automation Agent

A fully autonomous AI Sales Agent system that uses multiple personas to generate cold sales emails, evaluates them intelligently, and sends the best one to potential clients using email delivery services like Gmail or SendGrid.

## Features

- Three distinct sales agent tools to generate different email styles (formal, casual, witty)
- Manager agent autonomously evaluates and selects the best email
- Separate agents for subject line and HTML formatting
- Sends email via SendGrid using SendGrid API
- Designed for agentic workflows and autonomy

## Tech Stack

- Python 3.12
- Google Gemini (via `google.generativeai`) for content generation
- SendGrid for email generation and sending
- Jupyter Notebook for development and testing

## How It Works

1. Three AI agent "tools" generate email variants for a given product.
2. The Manager Agent tries each tool at least once, judges their outputs, and selects the best email.
3. A Subject Line Agent creates a compelling subject.
4. An HTML Formatter Agent styles the email body.
5. The final email is sent via SendGrid.
