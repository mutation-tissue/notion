from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# .envファイルの読み込み
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

sumerize_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "あなたは要約の天才です。入力された文章を要約してください。"),
        ("human","{text}")
    ]
)

quize_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "あなたはクイズ作成の天才です。入力されたテキストの内容から簡単、普通、難しいの３つの難易度の問題を3つずつ作成してください。また、最後にすべての問題に対して解説を簡単なものでよいので追記してください。"),
        ("human","{text}")
    ]
)
model = ChatOpenAI(model="gpt-4o-mini", temperature=0 ,openai_api_key = OPENAI_API_KEY)
StrOutputParser = StrOutputParser()

summerize_chain = sumerize_prompt | model | StrOutputParser
quize_chain = quize_prompt | model | StrOutputParser

def summerize_text(text:str) -> str:
    result = summerize_chain.invoke(text)
    header_text = f"元の文章：{len(text)}文字　要約された文章：{len(result)}文字\n"

    return header_text + result

def create_quize(text:str) -> str:
    result = quize_chain.invoke(text)
    header_text = f"ここからはクイズです。\n"

    return header_text + result