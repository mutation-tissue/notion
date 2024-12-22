import get_notion_content
import os

PARENT_PAGE_ID = os.getenv("PARENT_PAGE_ID")
# サブページの数を取得
data = get_notion_content.get_sub_page_ids(PARENT_PAGE_ID)
data = get_notion_content.get_sub_page_ids(data["results"][21]["id"])
data = get_notion_content.get_palan_text(data)

#pprint.pprint(data)