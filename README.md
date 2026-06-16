# 🐱 Kitty Tutor

## Project Objective

Kitty Tutor is an AI-powered study assistant designed to help students learn more efficiently. The application allows users to upload lecture notes in PDF format, generate summaries, create study quiz questions, and rewrite summaries in a more natural and human-friendly style.

---

## Features

- Upload PDF lecture notes
- Extract text from PDF files
- Generate AI summaries
- Generate AI quiz questions
- Humanize AI-generated summaries
- English and Finnish language support
- User-friendly Streamlit interface

---

## Tools Used

- Python
- Streamlit
- PyPDF2
- Hugging Face Transformers

---

## AI Models Used

### Summarization Model
- sshleifer/distilbart-cnn-12-6

### Text Generation Model
- google/flan-t5-base

The models are used for:
- Summarization
- Quiz generation
- Translation
- Humanization

---

## Project Architecture

Frontend:
- Streamlit

Backend:
- Hugging Face AI models

PDF Processing:
- PyPDF2

---

## Installation

Install required packages:

```bash
pip install streamlit
pip install PyPDF2
pip install transformers
pip install torch


How to Use
Upload a PDF file containing lecture notes.
Select English or Finnish language.
Click "Generate Summary" to create a summary.
Click "Humanize Summary" to rewrite the summary in a more natural style.
Click "Generate Quiz" to create study questions.








#streamlit run app.py

#cd backend
#uvicorn api:app --reload
