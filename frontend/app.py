import streamlit as st
import requests
from PIL import Image
import io

st.set_page_config(page_title="Receipt Parser", layout="centered")
st.title("🧾 Receipt OCR Parser")
st.write("Upload a receipt image or PDF, and extract key details!")

uploaded_file = st.file_uploader("Choose a receipt image or PDF", type=["jpg", "jpeg", "png", "pdf"])

if uploaded_file:
    # Show preview if image
    if uploaded_file.type.startswith("image/"):
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Receipt", use_column_width=True)

    st.write("⏳ Processing...")

    # Send file to backend
    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
    try:
        response = requests.post("http://127.0.0.1:8000/upload/", files=files)
        response.raise_for_status()
        result = response.json()["parsed_data"]

        st.success("✅ Extraction Complete")
        st.write("### Extracted Data:")
        st.json(result)
    except Exception as e:
        st.error(f"❌ Error: {e}")
