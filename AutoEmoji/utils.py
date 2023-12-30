import re

def extract_page_info(page_link):
    """
    Extracts the page ID and title from a Notion share link.

    Parameters:
    page_link (str): The Notion share link.

    Returns:
    tuple: The extracted page ID and title.
    """
    
    # extract page ID and title from link
    title_match = re.search(r'https://www.notion.so/ameenahmed/([\w-]+)-([\da-fA-F]{32})', page_link)
    
    if title_match:
        # format page ID into UUID format
        title = title_match.group(1).replace('-', ' ')
        unformatted_uuid = title_match.group(2)
        formatted_uuid = f"{unformatted_uuid[:8]}-{unformatted_uuid[8:12]}-{unformatted_uuid[12:16]}-{unformatted_uuid[16:20]}-{unformatted_uuid[20:]}" 
        return formatted_uuid, title
    
    else:
        raise ValueError("Invalid Notion link.")
