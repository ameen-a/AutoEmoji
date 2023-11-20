import requests
import os


NOTION_API_KEY = os.getenv('NOTION_API_KEY')



def update_page_icon(page_id, emoji):
    # Use the Notion API to update the page icon
    url = f"https://api.notion.com/v1/pages/{page_id}"

    # print(url)
    headers = {"Authorization": "Bearer " + NOTION_API_KEY,
                "Notion-Version": "2022-06-28",
                "Content-Type": "application/json"}
    data = {"icon": {"emoji": emoji}}
    # print("Updated to Notion!")
    requests.patch(url, headers=headers, json=data)
    response = requests.patch(url, headers=headers, json=data)
    print(response.text)


# page_id = "15618e2f-6d93-48e3-b446-34984f974bb0"

# emoji = "👋"
# url = f"https://api.notion.com/v1/pages/{page_id}"
# headers = {"Authorization": "Bearer " + NOTION_API_KEY,
#            "Notion-Version": "2022-06-28",
#            "Content-Type": "application/json"}
# data = {"icon": {"emoji": emoji}}
# print("Updated to Notion!")
# response = requests.patch(url, headers=headers, json=data)
# print(response.text)