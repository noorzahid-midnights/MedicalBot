# Medical Chatbot

This project is an AI-based medical chatbot that provides responses to user queries using LangChain, Pinecone for vector search, and Flask for deploying.

## Features

- Context-aware responses
- Semantic search using embeddings
- Query handling via API
- Retrieval-based response system

## Tech Stack

- Python
- Flask
- OpenAI API
- Pinecone (vector database)

## Project Structure

MedicalBot/
- app.py
- chatbot_logic/
- embeddings/
- templates/

## How It Works

1. User inputs a medical query
2. Query is converted into embeddings
3. Relevant information is retrieved from vector database
4. Response is generated and returned

## Future Improvements

- Integration with medical datasets
- Improved conversational memory
- Deployment with scalable backend
