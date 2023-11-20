from flask import Flask, request, render_template
from AutoEmoji.notion import update_page_icon
from AutoEmoji.gen_emoji import get_emoji
from AutoEmoji.utils import extract_page_info

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    emoji, page_name = None, None
    
    if request.method == 'POST':
        notion_link = request.form.get('notion_link')
        page_id, page_name = extract_page_info(notion_link)
        print(page_id, page_name)
        emoji = get_emoji(page_name)
        update_page_icon(page_id, emoji)
    return render_template('index.html', emoji=emoji, page_name=page_name)





# @app.route('/', methods=['GET', 'POST'])
# def home():
#     emoji = ''
#     if request.method == 'POST':
#         page_name = request.form.get('page_name')
#         page_link = request.form.get('page_link')
#         page_id = extract_page_id(page_link)
#         emoji = get_emoji(page_name)
#         update_page_icon(page_id, emoji)
#     return render_template('index.html', emoji=emoji)