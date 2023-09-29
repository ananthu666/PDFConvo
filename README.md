# PDFConvo

PDFConvo is an innovative document interaction system that empowers users to have dynamic conversations with PDF files. By leveraging advanced technologies like Langchain for PDF chunking, Faiss for similarity search, and OpenAI for natural language understanding, PDFConvo simplifies the way we work with PDF documents. Users can effortlessly upload PDFs, ask questions, and receive precise, context-aware responses. This project bridges the gap between static documents and interactive knowledge retrieval, promising to revolutionize document management, research, and education. Explore the pages ahead to discover how PDFConvo transforms PDFs into conversational partners, making information more accessible and actionable than ever before.

<img src="https://github.com/ananthu666/PDFConvo/blob/main/screenshot/pdf_convo_ss.png">

# [Link To Video](https://www.youtube.com/watch?v=YnownlTMzn8)

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
PDFConvo's functionality is built on three core components. Firstly, it employs Langchain to segment PDF documents, making them more manageable. Secondly, Faiss facilitates similarity searches, ranking results based on relevance. Lastly, OpenAI powers natural language understanding, enabling users to ask questions in plain language. Users can upload PDFs, pose questions, and receive context-aware answers. The system processes queries, matches them with relevant PDF sections, and delivers precise information. Overall, PDFConvo transforms static PDFs into interactive conversational partners, streamlining information retrieval across various domains.


## How to run
```bash
$ streamlit run streamlit_frontend.py
```


