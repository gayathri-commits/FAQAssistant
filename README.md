

# 🤖 FAQ Assistant Chatbot

A lightweight and smart FAQ chatbot that helps users find answers instantly by searching a CSV of questions & answers using vector similarity! Built with **Streamlit**, **Sentence Transformers**, and **FAISS**.

## 🧠 Features

* Upload a CSV file with `question` and `answer` columns
* Generates embeddings using `all-MiniLM-L6-v2`
* Uses FAISS to find the most similar FAQ based on user query
* Simple & beautiful Streamlit UI
* Fast, local, and no external API needed 💨

## 💾 Sample CSV Format

```csv
question,answer
How do I reset my password?,Go to settings and click reset password.
Where can I find the user manual?,It's available on the product page.
How to contact support?,Email us at support@example.com.
```

## 🧰 Tech Stack

* 🐍 Python
* 🧠 SentenceTransformers (`all-MiniLM-L6-v2`)
* 🧊 FAISS for vector search
* 🌐 Streamlit for UI

## 🛠️ How to Run

```bash
pip install streamlit faiss-cpu sentence-transformers pandas
streamlit run faq_assistant.py
```

## 📝 Preview

![Preview](image.png)

## 📌 Notes

* Make sure your CSV file **only contains `question` and `answer` columns**.
* Model runs locally and is great for offline or fast demos.

