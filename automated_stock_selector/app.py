import os
import warnings
import gradio as gr
from src.automated_stock_selector.crew import AutomatedStockSelector
from dotenv import load_dotenv

# Load environment variables from .env if needed
load_dotenv()

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run_crew(sector):
    if not sector:
        return "_❌ Please enter a sector._"
    
    try:
        inputs = {'sector': sector}
        AutomatedStockSelector().crew().kickoff(inputs=inputs)

        # Read markdown result
        markdown_path = os.path.join("output", "decision.md")
        if os.path.exists(markdown_path):
            with open(markdown_path, "r", encoding="utf-8") as f:
                markdown_content = f.read()
        else:
            markdown_content = "_⚠️ `decision.md` not found in output folder._"

        return markdown_content
    except Exception as e:
        return f"❌ Error during execution:\n\n```\n{str(e)}\n```"


# Gradio UI
with gr.Blocks(title="Automated Stock Selector") as demo:
    gr.Markdown("## 📈 Automated Stock Selector")

    sector_input = gr.Textbox(label="Enter Sector", placeholder="e.g., Technology, Healthcare, Energy")
    run_button = gr.Button("Run Selector", elem_id="run-btn")
    
    status_output = gr.Markdown()        # For the spinner/loading message
    markdown_output = gr.Markdown()      # For final decision.md content

    def run_with_spinner(sector):
        yield "⏳ Processing... Please wait.", ""
        result = run_crew(sector)
        yield "", result

    run_button.click(fn=run_with_spinner, 
                     inputs=sector_input, 
                     outputs=[status_output, markdown_output])
    demo.css = """
    #run-btn {
        background-color: #18181b !important;  
        color: white !important;
        font-weight: bold !important;
        border-radius: 8px !important;
    }
    #run-btn:hover {
        background-color: #59168a !important; 
    }
    """

# Launch the app
if __name__ == "__main__":
    demo.launch()
