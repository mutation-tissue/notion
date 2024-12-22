import get_notion_content
import post_notion_content
import langchain_task
from dotenv import load_dotenv
import os
import pprint
from time import sleep
# .envファイルの読み込み
load_dotenv()
PARENT_PAGE_ID = os.getenv("PARENT_PAGE_ID")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def create_summrize_quize(sub_page_id,sub_page_title):
    sub_page_data =get_notion_content.get_sub_page_ids(sub_page_id)
    sub_page_url = get_notion_content.get_page_url(sub_page_title) + "-" + sub_page_id.replace("-","")

    #テキストのみ取得
    plain_text = get_notion_content.get_palan_text(sub_page_data)

    #langchainを使ってサブページの内容を要約
    summerize_text = langchain_task.summerize_text(plain_text)
    quize_text = langchain_task.create_quize(plain_text)

    #notionに新しいサブページとして追加する。
    post_notion_content.send_request(sub_page_title,sub_page_url,summerize_text,quize_text)

def main():
    # サブページの数を取得
    parent_data = get_notion_content.get_sub_page_ids(PARENT_PAGE_ID)

    while True:
        next_cursor = parent_data.get("next_cursor")
        sub_pages += [x  for x in parent_data["results"] if x["type"]=="child_page"]
        sleep(3)
        if not parent_data.get("has_more"):
            break
        
        parent_data = get_notion_content.get_sub_page_ids(PARENT_PAGE_ID,next_cursor)

    #すでに要約を作っているか確認する機能が必要
    for sub_page in sub_pages:
        # sub_page_id = parent_data["results"][21]["id"]
        #サブページ内のURLを取得する
        sub_page_title = sub_page["child_page"]["title"]
        # sub_page_id = sub_page["id"]
        # create_summrize_quize(sub_page_id, sub_page_title)
        print(sub_page_title)


if __name__ == "__main__":
    main()