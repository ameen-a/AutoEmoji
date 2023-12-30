<div align="center">
  <img src="https://github.com/ameen-a/AutoEmoji/assets/7096331/3923ce1e-40da-4532-a3b8-8155def4b438" alt="Notion AutoEmoji", width="650">
</div>


# Notion AutoEmoji
### Intelligently chosen emojis for your Notion pages. Powered by LLMs and deployed to the cloud. 

**Problem Statement:** When you select 'Add Icon' to a Notion page, a _random_ emoji is assigned to it. I found this behavior deeply unsatisfying, so I decided to fix it by letting an LLM pick one instead. 
This project was written in Python with a simple front-end built using HTML/CSS/JS, containerised using Docker, and deployed to AWS ECS for personal use. You can achieve pretty good performance using `model="gpt-3.5-turbo"`, but feel free to swap to `gpt-4` for extra overkill. 

<div align="center">
  <img src="https://raw.githubusercontent.com/ameen-a/AutoEmoji/main/AutoEmoji/assets/AutoEmoji%20gif.gif" alt="Usage demonstration", width="700">
</div>

## Usage:
- Create a new Notion page and give it a title.
- On the top-right of the Notion window, click `Share` and then `Copy Link`.
- Paste the link into the _AutoEmoji_ text box and click `Get Emoji`.


### Prerequisites
- openai (`pip install openai`)
- notion (`pip install notion`)
- flask (`pip install flask`) _if running on a local web server_


### Installation steps:
- Create a new [Notion integration](https://www.notion.so/my-integrations) and find your [OpenAI API key](https://platform.openai.com/api-keys), saving both as environment variables. 
- Give your desired Notion pages access to the integration you just created. <img width="500" alt="image" src="https://github.com/ameen-a/AutoEmoji/assets/7096331/6bfb3230-b5b7-4ddd-add7-0fce64a07628">
- To run the front-end locally, navigate to the root directory and run the command `export FLASK_APP=AutoEmoji/main.py` followed by `flask run`. A new browser window should appear. 

### Example emoji suggestions

<div align="center">
  <img width="500" alt="image" src="https://github.com/ameen-a/AutoEmoji/assets/7096331/df9c9df1-cec6-4629-8ee0-19aedee139f8">
</div>

My favorites: 

🏢 Jane Street - not only does the model recognise Jane Street as an entity, it captures the firm's high-corporate finance vibe with an office building emoji. 
🌎 Effective Altruism - there are several good candidates for this: 💡, 🤝, ❤, 🌱, 📊, 🧠, 🔬, 📚, 💸, etc., yet I think the model found the best one. 



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


## Authors

* **Ameen Ahmed** - [ameen-a](https://github.com/ameen-a)

