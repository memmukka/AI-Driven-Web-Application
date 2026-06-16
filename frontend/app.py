import streamlit as st
from PyPDF2 import PdfReader
from transformers import pipeline


st.set_page_config(
    page_title="Kitty Tutor",
    page_icon="🐱",
    layout="centered"
)


st.markdown("""
<style>
.stApp {
    background-color: #FFF5F7;
}

h1 {
    color: #FF69B4;
    text-align: center;
}

div.stButton > button {
    border-radius: 12px;
    background-color: #FFD6E7;
    color: black;
    border: none;
}

div.stButton > button:hover {
    background-color: #FFB6D5;
}

section[data-testid="stSidebar"] {
    background-color: #FFE4EF;
}
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_models():

    summarizer = pipeline(
        "summarization",
        model="sshleifer/distilbart-cnn-12-6"
    )

    generator = pipeline(
        "text2text-generation",
        model="google/flan-t5-base"
    )

    return summarizer, generator

summarizer, generator = load_models()


st.markdown("<h1>🐱 Kitty Tutor 📚</h1>", unsafe_allow_html=True)
st.write("Your AI study buddy ")


language = st.selectbox(
    "🌍 Select Language",
    ["English", "Finnish"]
)


uploaded_file = st.file_uploader(
    "📄 Upload your lecture notes",
    type="pdf"
)

if uploaded_file is not None:

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    
    text = text.replace("\n", " ")
    text = " ".join(text.split())

    with st.expander("📖 View Extracted Text"):
        st.write(text[:4000])

   
    if st.button("🐱 Generate Summary"):

        with st.spinner("🐱 Kitty is reading your notes..."):

            summary = summarizer(
                text[:4000],
                max_length=150,
                min_length=50,
                do_sample=False
            )

            summary_text = summary[0]["summary_text"]

            if language == "Finnish":

                translation_prompt = f"""
Translate the following text into Finnish:

{summary_text}
"""

                translated = generator(
                    translation_prompt,
                    max_length=300
                )

                summary_text = translated[0]["generated_text"]

            st.session_state.summary_text = summary_text

            st.success("Summary generated!")
            st.subheader("🐱 Summary")
            st.info(summary_text)

    
    if "summary_text" in st.session_state:

        if st.button("✨ Humanize Summary"):

            with st.spinner("🐱 Kitty is making the summary sound more human..."):

                humanizer_prompt = f"""
Rewrite this summary so it sounds natural, friendly, and written by a university student.

Keep all important information.

Summary:
{st.session_state.summary_text}
"""

                humanized = generator(
                    humanizer_prompt,
                    max_length=300
                )

                humanized_text = humanized[0]["generated_text"]

                if language == "Finnish":

                    translation_prompt = f"""
Translate the following text into Finnish:

{humanized_text}
"""

                    translated = generator(
                        translation_prompt,
                        max_length=400
                    )

                    humanized_text = translated[0]["generated_text"]

                st.success("Humanized summary generated!")
                st.subheader("Humanized Summary")
                st.info(humanized_text)

    
    if st.button("📝 Generate Quiz"):

        with st.spinner("🐱 Kitty is making quiz questions..."):

            prompt = f"""
Create 5 clear study questions for a university student based on these notes.

Only output the questions as a numbered list.

{text[:2000]}
"""

            result = generator(
                prompt,
                max_length=200
            )

            quiz_text = result[0]["generated_text"]

            if language == "Finnish":

                translation_prompt = f"""
Translate the following quiz questions into Finnish:

{quiz_text}
"""

                translated = generator(
                    translation_prompt,
                    max_length=300
                )

                quiz_text = translated[0]["generated_text"]

            st.success("Quiz generated!")
            st.subheader("📝 Quiz Questions")
            st.info(quiz_text)