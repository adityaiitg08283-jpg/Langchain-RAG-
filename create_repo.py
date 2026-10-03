import os

repo_name = "Langchain-Course-Repo"

# Folder structure based on CampusX playlist
folders = [
    "01-Introduction-and-Components",
    "02-Models-and-Prompts",
    "03-Structured-Output-and-Parsers",
    "04-Chains-and-LCEL",
    "05-Data-Ingestion-and-RAG",
    "06-Agents-and-Tools",
    "07-Projects/01_youtube_rag_chatbot",
    "07-Projects/02_local_llms_ollama"
]

# File contents with starter codes
files = {
    "README.md": """# 🦜🔗 Generative AI using LangChain

This repository contains code implementations, notes, and projects based on the **Generative AI using LangChain** playlist by **CampusX**.

## 🛠️ Setup Instructions
1. `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and add your API keys.
""",
    "requirements.txt": "langchain\nlangchain-openai\nlangchain-community\nlangchain-core\nchromadb\nfaiss-cpu\npython-dotenv\n",
    ".env.example": "OPENAI_API_KEY=your_openai_api_key_here\nHUGGINGFACEHUB_API_TOKEN=your_hf_token_here\n",
    ".gitignore": ".env\nvenv/\n__pycache__/\n*.ipynb_checkpoints/\n",
    
    # Module 2: Models & Prompts
    "02-Models-and-Prompts/01_llms.py": """from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
chat_model = ChatOpenAI(model='gpt-3.5-turbo')
response = chat_model.invoke("Explain LangChain in one sentence.")
print(response.content)
""",
    "02-Models-and-Prompts/02_prompt_templates.py": """from langchain_core.prompts import PromptTemplate

template = "Translate the following English sentence to {language}: {sentence}"
prompt = PromptTemplate.from_template(template)
print(prompt.format(language="Hindi", sentence="Machine Learning is fascinating!"))
""",

    # Module 4: LCEL
    "04-Chains-and-LCEL/01_lcel_basics.py": """from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()
prompt = PromptTemplate.from_template("Tell me a short joke about {topic}")
parser = StrOutputParser()

# LCEL Chain
chain = prompt | model | parser
print(chain.invoke({"topic": "programmers"}))
""",

    # Module 5: RAG
    "05-Data-Ingestion-and-RAG/01_document_loaders.py": """from langchain_community.document_loaders import TextLoader

# loader = TextLoader("sample.txt")
# docs = loader.load()
# print(docs)
print("This module covers TextLoader, PyPDFLoader, and WebBaseLoader.")
"""
}

# Create base repo directory
os.makedirs(repo_name, exist_ok=True)

# Create folders
for folder in folders:
    os.makedirs(os.path.join(repo_name, folder), exist_ok=True)

# Create files and inject code
for filepath, content in files.items():
    full_path = os.path.join(repo_name, filepath)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"✅ Success! Your complete '{repo_name}' has been generated locally.")
print("Ab is folder ko open karein aur apna GitHub push command chala dein!")
