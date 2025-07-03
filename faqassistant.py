# 💾 Requirements: pip install streamlit faiss-cpu sentence-transformers pandas

import streamlit as st
import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

st.set_page_config(page_title="💬 Product FAQ Assistant")
st.title("📄 Smart FAQ Assistant")
st.caption("Upload a CSV file with 'question' and 'answer' columns. Ask a question and get the most relevant answer instantly!")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# File upload
uploaded_file = st.file_uploader("📥 Upload your FAQ CSV", type=["csv"])

# Globals
faq_index = None
faq_data = None

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    if "question" not in df.columns or "answer" not in df.columns:
        st.error("❌ CSV must contain 'question' and 'answer' columns.")
    else:
        with st.spinner("Embedding your FAQs..."):
            faq_data = df
            faq_embeddings = model.encode(faq_data['question'].tolist())
            faq_index = faiss.IndexFlatL2(faq_embeddings.shape[1])
            faq_index.add(np.array(faq_embeddings))

        st.success("✅ FAQ indexed! Ask away 💬")

# Query section
if faq_index is not None:
    user_query = st.text_input("❓ Ask a question")
    if user_query:
        query_embedding = model.encode([user_query])
        D, I = faq_index.search(np.array(query_embedding), k=3)

        st.markdown("### 🔍 Most Relevant Answer:")
        top_idx = I[0][0]
        st.write(f"**Q:** {faq_data.iloc[top_idx]['question']}")
        st.success(f"**A:** {faq_data.iloc[top_idx]['answer']}")

        # Optional: show others
        st.markdown("---")
        st.markdown("### 🪄 Other similar questions:")
        for i in I[0][1:]:
            st.write(f"• {faq_data.iloc[i]['question']}")
