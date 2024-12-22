import requests
import os
import pprint

# 環境変数を取得
API_KEY = os.getenv("NOTION_API_KEY")
PARENT_PAGE_ID = os.getenv("PARENT_PAGE_ID")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Notion-Version": "2022-06-28",
}

def get_sub_page_ids(parent_page_id):
    """親ページ内のサブページ数をカウントする"""
    url = f"https://api.notion.com/v1/blocks/{parent_page_id}/children"
    response = requests.get(url, headers=headers)
    data = response.json()
    sub_page_ids = [
        block["id"] for block in data.get("result", [])
        if block["type"] == "child_page"
    ]
    return data

def get_palan_text(sub_page_data):
    for data in sub_page_data["results"]:
        if(data):
            try:
                print("----------------paragraph------------")
                print(data["paragraph"]["rich_text"][0]["plain_text"])
                print(data["type"])
            except:
                print("----------------取得できませんでした------------")
                print(data["type"])
                pass