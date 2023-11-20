
import re

def extract_page_info(page_link):
    """
    Extracts the page ID and title from a Notion share link.

    Parameters:
    page_link (str): The Notion share link.

    Returns:
    tuple: The extracted page ID and title.
    """
    print(page_link)

    
    title_match = re.search(r'https://www.notion.so/ameenahmed/([\w-]+)-([\da-fA-F]{32})', page_link)
    
    if title_match:
        title = title_match.group(1).replace('-', ' ')
        unformatted_uuid = title_match.group(2)
        # Check the length of the unformatted UUID to ensure it's 32 characters long
        # if len(unformatted_uuid) != 32:
        #     raise ValueError(f"Invalid UUID format: {unformatted_uuid}")
        # Reformats the UUID to the correct format [8, 4, 4, 4, 12]
        # reformat uuid to match the standard 8-4-4-4-12 format
        formatted_uuid = f"{unformatted_uuid[:8]}-{unformatted_uuid[8:12]}-{unformatted_uuid[12:16]}-{unformatted_uuid[16:20]}-{unformatted_uuid[20:]}"
        print(f"Title: {title}")
        print(f"Formatted UUID: {formatted_uuid}")     
        return formatted_uuid, title
    else:
        raise ValueError("Invalid Notion link.")





# def extract_page_id(page_link):
#     # Extracting the raw uuid from the url
#     raw_uuid = re.search(r'-(.*?)[^a-f0-9]', page_link)
#     if raw_uuid is None:
#         return "Invalid URL or UUID not found."
#     else:
#         raw_uuid = raw_uuid.group(1)

#     # Adding hyphens to split the uuid into chunks of [8, 4, 4, 12]
#     uuid = '-'.join([raw_uuid[i:j] for i, j in zip([0, 8, 12, 16, 20], [8, 12, 16, 20, 32])])

#     return uuid











# # import re
# def extract_page_id(page_link):
#     path = urllib.parse.urlparse(page_link).path
#     path_parts = path.split(b'/')
#     if len(path_parts) > 2:
#         raw_id = '-'.join(path_parts[2:])
#         uuid = re.search(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', raw_id)
#         return uuid.group(0) if uuid else "Invalid URL"
#     else:
#         return "Invalid URL"





# def extract_page_id(page_link):
#     """
#     Extracts the page ID from a Notion share link.

#     Parameters:
#     notion_link (str): The Notion share link.

#     Returns:
#     str: The extracted page ID.
#     """
#     match = re.search(r'([a-f0-9]{32})', page_link.replace('-', ''))
#     if match:
#         uuid = match.group(1)
#         return '-'.join([uuid[i:i+length] for i, length in zip(range(0, len(uuid)), [8, 4, 4, 4, 12])])
#     else:
#         raise ValueError("Invalid Notion link.")

    

# notion_link = "https://www.notion.so/ameenahmed/Cooking-0a302c1f73d14c38a144d1b87c595709?pvs=4"

 
# page_id = extract_page_id(notion_link)
# print(page_id)
# https://www.notion.so/ameenahmed/Cooking-0a302c1f73d14c38a144d1b87c595709?pvs=4