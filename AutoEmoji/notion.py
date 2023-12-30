import requests
import os

NOTION_API_KEY = os.getenv('NOTION_API_KEY')

def update_page_icon(page_id, emoji):
    """
    Updates the icon of a Notion page.
    
    Parameters:
    page_id (str): The ID of the Notion page.
    emoji (str): The emoji to set as the page icon.
    
    Returns:
    None
    """
    
    # get payload
    url = f"https://api.notion.com/v1/pages/{page_id}"
    headers = {"Authorization": "Bearer " + NOTION_API_KEY,
                "Notion-Version": "2022-06-28",
                "Content-Type": "application/json"}
    data = {"icon": {"emoji": emoji}}

    # send PATCH request to update the page icon
    requests.patch(url, headers=headers, json=data)
    response = requests.patch(url, headers=headers, json=data)