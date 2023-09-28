from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader
# //////////////////////
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
import textwrap
from pdf_text import texter
# //////////////

embeddings = OpenAIEmbeddings(openai_api_key='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')


def loading(filename):
    if(filename):
        text=texter(filename)
        
        # loader = PyPDFLoader(filename)
        # pages = loader.load_and_split()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        docs = text_splitter.split_text(text)
        db = FAISS.from_texts(docs, embeddings)
        return db


def get_response(db, query, k=4):
    docs = db.similarity_search(query, k=k)
    docs_page_content = " ".join([d.page_content for d in docs])

    chat = ChatOpenAI(model_name="gpt-3.5-turbo-16k", temperature=0.2,openai_api_key="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")

    # Template to use for the system message prompt
    template = """
        You are a helpful assistant that that can answer questions about contents of pdf files 
        based on the pdf transcript: {docs}
        
        Only use the factual information from the transcript to answer the question.
        
        If you feel like you don't have enough information to answer the question, say "I don't know".
        
        """

    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    # Human question prompt
    human_template = "Answer the following question: {question}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(
        human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)

    response = chain.run(question=query, docs=docs_page_content)
    response = response.replace("\n", "")
    return response, docs


# query = "what is best fit?"
# response, docs = get_response(db, query)
# print(textwrap.fill(response, width=50))
