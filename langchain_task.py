from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# .envファイルの読み込み
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "あなたは要約の天才です。入力された文章を要約してください。"),
        ("human","{text}")
    ]
)
model = ChatOpenAI(model="gpt-4o-mini", temperature=0 ,openai_api_key = OPENAI_API_KEY)
StrOutputParser = StrOutputParser()

chain = prompt | model | StrOutputParser

def summerize_text(text:str) -> str:
    result = chain.invoke(text)
    header_text = f"元の文章：{len(text)}文字　要約された文章：{len(result)}文字\n"

    return header_text + result