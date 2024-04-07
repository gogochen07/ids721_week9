import streamlit as st
from transformers import pipeline

# Load the language model
model = pipeline("text-generation", model="openai-gpt")

# Define Streamlit app with enhanced aesthetics, additional content, and fancy styling
def main():
    # Set page title and add some styling
    st.set_page_config(page_title="Tweet", page_icon="🤖")
    st.title("Text Generation with Hugging Face Transformers")
    st.markdown("This mini-app generates Text using Hugging Face Transformers. ")
    
    # Add text input area with placeholder
    topic = st.text_input(label="Topic (or promopt)", placeholder="your text here")
    
    # Add generate button with custom styling
    st.markdown("<style> .stButton button {background-color: #2a9d8f; color: white;}</style>", unsafe_allow_html=True)
    st.write("")
    if st.button("Generate", key="generate_button", help="Click to generate text"):
        if topic:
            # Generate text with the language model
            generated_text = model(topic, max_length=50, do_sample=True)[0]['generated_text']
            
            # Display generated text with styling
            # st.markdown("## Generated Text:")
            header_html = f"""
            <h1 style="color: white; text-align: center;">Generated Text</h1>
            <div>
                {generated_text}
            </div>
            """
            st.markdown(header_html, unsafe_allow_html=True)
        else:
            # Display warning if no text input
            st.warning("Please enter some text first.")

if __name__ == "__main__":
    main()