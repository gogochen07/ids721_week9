import streamlit as st
from transformers import pipeline

model = pipeline("text-generation", model="openai-gpt")

def main():
    st.set_page_config(page_title="IDS721")
    st.title("Text Generation with Hugging Face Transformers (Yuwen Chen ids721_week9)")
    st.markdown("This mini-app generates Text using Hugging Face Transformers. ")

    topic = st.text_input(label="Topic (or promopt)", placeholder="your text here")
    
    st.markdown("<style> .stButton button {background-color: #2a9f8f; color: orange;}</style>", unsafe_allow_html=True)
    st.write("")
    if st.button("Go", key="generate_button", help="Click to generate text"):
        if topic:
            generated_text = model(topic, max_length=50, do_sample=True)[0]['generated_text']
            header_html = f"""
            <h1 style="color: black; text-align: center;">Generated Text</h1>
            <div>
                {generated_text}
            </div>
            """
            st.markdown(header_html, unsafe_allow_html=True)
        else:
            st.warning("Empty text input.")

if __name__ == "__main__":
    main()