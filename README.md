MedicalBot - AI Powered Medical Chatbot
Overview

MedicalBot is a Retrieval-Augmented Generation (RAG) based chatbot that answers medical-related queries using a vector database and Google Gemini AI model. It retrieves relevant medical information from stored embeddings and generates accurate responses using LLMs.

Features
Medical question answering using AI
RAG pipeline with Pinecone vector database
Embedding generation using Sentence Transformers
Google Gemini (ChatGoogleGenerativeAI) for response generation
Flask web interface for user interaction
Tech Stack
Python
Flask
LangChain
Pinecone Vector DB
Google Gemini API
Sentence Transformers (HuggingFace embeddings)
Project Structure

MedicalBot/
│
├── app.py
├── src/
│ ├── helper.py
│ ├── prompt.py
├── templates/
├── static/
├── requirements.txt
├── README.md

Setup Instructions
1. Clone repository

git clone <your-repo-link>

2. Create virtual environment

python -m venv venv
venv\Scripts\activate (Windows)

3. Install dependencies

pip install -r requirements.txt

4. Set environment variables

Create a .env file:

GOOGLE_API_KEY=your_api_key
PINECONE_API_KEY=your_api_key

5. Run the application

python app.py

How it works
User asks a question
Query is converted into embeddings
Pinecone retrieves relevant documents
Gemini generates final answer using context
Flask returns response to UI
Notes
Make sure API keys are valid
Use Python 3.10–3.11 for best compatibility
