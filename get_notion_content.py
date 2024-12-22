import requests
import os
import re
import pprint

# 環境変数を取得
API_KEY = os.getenv("NOTION_API_KEY")
PARENT_PAGE_ID = os.getenv("PARENT_PAGE_ID")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Notion-Version": "2022-06-28",
}

def get_sub_page_ids(parent_page_id,next_cursor=None):
    """親ページ内のサブページ数をカウントする"""
    url = f"https://api.notion.com/v1/blocks/{parent_page_id}/children"

    # ペイロードの作成
    params = {
        "page_size": 100
    }
    if next_cursor:
        params["start_cursor"] = next_cursor

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    sub_page_ids = [
        block["id"] for block in data.get("result", [])
        if block["type"] == "child_page"
    ]
    return data

def get_page_url(input_text):
    """
    半角のアルファベット、数字、記号の連続部分を抽出し、-で連結する
    :param input_text: 処理対象の文字列
    :return: 抽出した文字列を-で連結した結果
    """
    # 正規表現パターン：半角のアルファベット、数字、記号の連続部分
    pattern = r'[A-Za-z0-9]+'
    
    # マッチした部分をリストとして取得
    matches = re.findall(pattern, input_text)
    
    # リストを'-'で連結して返す
    return "https://www.notion.so/" + '-'.join(matches)


def get_palan_text(sub_page_data):
    plain_text = ""
    for data in sub_page_data["results"]:
        try:
            if(data["paragraph"]):
                """print("----------------paragraph------------")
                print(data["paragraph"]["rich_text"][0]["plain_text"])
                print(data["type"])"""
                plain_text += data["paragraph"]["rich_text"][0]["plain_text"] + "\n"

        except:
            #print("----------------取得できませんでした------------")
            #print(data["type"])
            pass
    return plain_text