import requests
import os

# 環境変数を取得
API_KEY = os.getenv("NOTION_API_KEY")
PARENT_PAGE_ID = os.getenv("PARENT_PAGE_ID")

print(f"API_KEY: {API_KEY}")
print(f"PARENT_PAGE_ID: {PARENT_PAGE_ID}")

