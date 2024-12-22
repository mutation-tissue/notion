import get_notion_content
import post_notion_content
import langchain_task
from dotenv import load_dotenv
import os

# .envファイルの読み込み
load_dotenv()
PARENT_PAGE_ID = os.getenv("PARENT_PAGE_ID")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def main():
    # サブページの数を取得
    parent_data = get_notion_content.get_sub_page_ids(PARENT_PAGE_ID)
    
    #サブページ内のURLを取得する
    sub_page_title = parent_data["results"][21]["child_page"]["title"]
    sub_page_url = get_notion_content.get_page_url(sub_page_title) + "-" + sub_page_title["results"][21]["id"].replace("-","")
    print(sub_page_url)

    #サブページの内容を取得
    sub_page_data = get_notion_content.get_sub_page_ids(sub_page_data["results"][21]["id"])
    
    #テキストのみ取得
    plain_text = get_notion_content.get_palan_text(sub_page_data)

    #langchainを使ってサブページの内容を要約
    summerize_text = langchain_task.summerize_text(plain_text)

    #notionに新しいサブページとして追加する。
    post_notion_content.send_request(sub_page_title,summerize_text,sub_page_url)



if __name__ == "__main__":
    main()