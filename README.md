# 📝 Text Summarizer App

A simple Generative AI project that summarizes long text, `.txt`, or `.pdf` files using Hugging Face Transformers and Gradio.

## 🔍 Features
- Summarize **pasted text**, **.txt files**, or **.pdf files**
- Clean and interactive **Gradio UI**
- Uses the `facebook/bart-large-cnn` model for summarization
- Works on **CPU** (no GPU required)
- Minimal setup with `requirements.txt`

## 🚀 How to Run Locally

1. **Clone the repository**

git clone https://github.com/yourusername/text-summarizer-app.git
cd text-summarizer-app

Install dependencies
pip install -r requirements.txt

Run the app
python text-summary.py
Access the app

Open http://127.0.0.1:7860 in your browser.

🧠 Model Used
facebook/bart-large-cnn

📁 File Structure
bash
Copy
Edit
text-summarizer-app/
│
├── text-summary.py       # Main application code
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
📦 Requirements
See requirements.txt for all dependencies.

📄 License
This project is licensed under the MIT License.
