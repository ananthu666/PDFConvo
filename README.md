# PDFConvo



<img src="https://github.com/ananthu666/PDFConvo/blob/main/screenshot/pdf_convo_ss.png">

# [Link To Video](./)

# [Chat with Bot](./)

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites And Installation](#prerequisites-and-installation)
- [Working](#working)
- [How to Run](#how-to-run)

## Features
- **User-Friendly Chat Interface**:Provides an intuitive chat-based interface for users to interact with the system.

- **Query Submission**:Allows users to submit natural language queries to search for information within PDF documents.

- **Full-Text Search**:Enables users to perform full-text searches within selected PDF sections.

- **Query History**:Provides access to the user's query history for easy reference and revisiting previous interactions.

## Getting Started

``` Clone The Repo PDFConvo```

### Prerequisites And Installation

```
langchain==0.0.300
faiss-cpu==1.7.4
openai==0.27.8
simplejson==3.19.1
dataclasses-json==0.6.0
requests==2.28.2
requests-oauthlib==1.3.1
PyPDF2==3.0.1
```
```bash
pip install -r requirements.txt
```

## Working 
PDFConvo is a sophisticated and user-centric document interaction system designed to streamline the way users engage with PDF files. It combines cutting-edge technologies like Langchain for PDF chunking, Faiss for similarity search, and OpenAI for natural language processing. Users can effortlessly upload their PDF documents, ask questions, and receive relevant information from within those documents. The system processes user queries, identifies context and intent, and retrieves pertinent content from the uploaded PDFs. It offers an intuitive chatbot interface, making it user-friendly and accessible. PDFConvo is a versatile tool suitable for various domains, from research and education to business and personal use. It simplifies document retrieval, enhances user experiences, and empowers users to harness the potential of their PDF files effectively.


## How to run
```bash
$ streamlit run newfront.py
```


