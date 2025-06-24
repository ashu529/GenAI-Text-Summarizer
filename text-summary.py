import gradio as gr
from transformers import pipeline
import fitz  # PyMuPDF

# Load the summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Extract text from PDF
def extract_text_from_pdf(pdf_file):
    try:
        with fitz.open(pdf_file.name) as doc:
            return "\n".join([page.get_text() for page in doc])
    except Exception as e:
        return f"❌ PDF Error: {str(e)}"

# Main summarization logic
def summarize_input(text, file):
    input_text = ""

    if text.strip():
        input_text += text

    if file is not None:
        if file.name.endswith(".txt"):
            try:
                with open(file.name, "r", encoding="utf-8", errors="ignore") as f:
                    input_text += "\n" + f.read()
            except Exception as e:
                return f"❌ TXT Error: {str(e)}"
        elif file.name.endswith(".pdf"):
            extracted = extract_text_from_pdf(file)
            if extracted.startswith("❌ PDF Error:"):
                return extracted
            input_text += "\n" + extracted

    if not input_text.strip():
        return "❗ Please enter text or upload a valid .txt or .pdf file."

    # Truncate long input
    if len(input_text) > 4000:
        input_text = input_text[:4000]

    try:
        summary = summarizer(input_text, max_length=130, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"❌ Summarization Error: {str(e)}"

# Gradio Interface (no title shown)
interface = gr.Interface(
    fn=summarize_input,
    inputs=[
        gr.Textbox(lines=10, placeholder="Enter or paste text here...", label="📥 Input Text"),
        gr.File(label="📄 Upload .txt or .pdf", file_types=[".txt", ".pdf"])
    ],
    outputs=gr.Textbox(label="📝 Summary", show_copy_button=True),
    title="",
    description="Paste text or upload a .txt/.pdf file to get a summary.",
    flagging_mode="never"
)

interface.launch()

