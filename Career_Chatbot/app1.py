from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader
import gradio as gr
import os

load_dotenv(override=True)

reader = PdfReader("me/M Kopika.pdf")
linkedin = ""
for page in reader.pages:
    text = page.extract_text()
    if text:
        linkedin += text
reader1 = PdfReader("me/Profile.pdf")
for page in reader1.pages:
    text = page.extract_text()
    if text:
        linkedin += text

with open("me/summary.txt", "r", encoding="utf-8") as f:
    summary = f.read()

name = "M Kopika"

system_prompt = f"You are acting as {name}. You are answering questions on {name}'s portfolio website, \
particularly questions related to {name}'s career, background, skills and experience. \
Your responsibility is to represent {name} for interactions on the website as faithfully as possible. \
You are given a summary of {name}'s background and LinkedIn profile which you can use to answer questions. \
Be professional and engaging, as if talking to a potential client or future employer who came across the website. \
If you don't know the answer, say so and suggest the user to send their queries to {name}'s mail which is kopika0208@gmail.com. Show the {name}'s mail id as a hyperlink leading to mail."

system_prompt += f"\n\n## Summary:\n{summary}\n\n## LinkedIn Profile:\n{linkedin}\n\n"
system_prompt += f"With this context, please chat with the user, always staying in character as {name}."

google_api_key = os.getenv('GOOGLE_API_KEY')

gemini=OpenAI(api_key=google_api_key,base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
def chat(message, history):
    messages = [{"role": "system", "content": system_prompt}] + history + [{"role": "user", "content": message}]
    response = gemini.chat.completions.create(model="gemini-2.0-flash", messages=messages)
    return response.choices[0].message.content

if __name__ == "__main__":
    gr.ChatInterface(chat, type="messages").launch()


