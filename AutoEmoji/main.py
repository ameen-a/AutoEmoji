from flask import Flask, request, render_template
from AutoEmoji.notion import update_page_icon
from AutoEmoji.gen_emoji import get_emoji
from AutoEmoji.utils import extract_page_info

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Renders the home page.
    
    Parameters:
    None
    
    Returns:
    str: The rendered HTML page.
    """

    emoji, page_name = None, None
    
    # if POST request, update the page icon
    if request.method == 'POST':
        notion_link = request.form.get('notion_link')
        page_id, page_name = extract_page_info(notion_link)
        emoji = get_emoji(page_name)
        update_page_icon(page_id, emoji)

    return render_template('index.html', emoji=emoji, page_name=page_name)
