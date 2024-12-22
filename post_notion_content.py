import requests
import os
from dotenv import load_dotenv
import pprint

# 環境変数を取得
load_dotenv()
API_KEY = os.getenv("NOTION_API_KEY")
WRITE_PAGE_ID = os.getenv("WRITE_PAGE_ID")
# APIエンドポイント
sub_page_url = f"https://api.notion.com/v1/pages"

# ヘッダー設定
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}

# 書き込み内容
template = {
    "parent": {"type": "page_id", "page_id": WRITE_PAGE_ID},
    "properties": {
        "title": [
            {
                "text": {
                    "content": "ここにタイトルを入力"
                }
            }
        ]
    },
    "children": [
        {
            "object": "block",
            "type": "paragraph",
            'paragraph': {
                'rich_text': [
                    {'type': 'text',
                    'text': {
                        'content': 'https://news.mynavi.jp/techplus/article/20231222-2847330/',
                            'link': {
                                'url': 'https://news.mynavi.jp/techplus/article/20231222-2847330/'
                                }
                    }
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "これはサンプルの段落テキストです。",
                        }
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "これはサンプルの段落テキストです。",
                        }
                    }
                ]
            }
        }
    ]
}

"今後はcreateに変更して複数のURLやテキストを追加できるようにする予定"
def  update_template(title, url, summerize, quize):
    new_template = template.copy()
    new_template["properties"]["title"][0]["text"]["content"] = title
    new_template["children"][0]["paragraph"]["rich_text"][0]["text"]["content"] = "要約元ページ(notion内)"
    new_template["children"][0]["paragraph"]["rich_text"][0]["text"]["link"]["url"] = url
    new_template["children"][1]["paragraph"]["rich_text"][0]["text"]["content"] = summerize
    new_template["children"][2]["paragraph"]["rich_text"][0]["text"]["content"] = quize

    return new_template

def send_request(title, source_url, summerize, quize):
    # リクエスト送信
    print(sub_page_url)
    send_message = update_template(title, source_url, summerize, quize)
    response = requests.post(sub_page_url, headers=headers, json=send_message)

    # レスポンス確認
    if response.status_code == 200:
        print("文字を書き込みました！")
    else:
        print("エラー:", response.status_code, response.text)
