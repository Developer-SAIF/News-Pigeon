import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from extract_news import extract_news_details
import requests

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

def fetch_and_save_news(page):
    url = "https://www.thedailystar.net/views/ajax"
    payload = f"page={page}&view_name=category_load_more_news&view_display_id=panel_pane_1&view_args=283517%2F%2F3884096%2C3884081%2C3884021%2C3884016%2C3883971%2C3883961%2C3883951%2C3883916%2C3883911%2C3883906%2C3883881%2C3883866%2C3883856%2C3883831%2C3883806%2C3883786%2C3883781%2C3883046&view_path=taxonomy%2Fterm%2F283517&view_base_path=&view_dom_id=f631e9a266accce62ec361480fa77ef0&pager_element=0&ajax_html_ids%5B%5D=fb-root"
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
    }
    response = requests.post(url, headers=headers, data=payload)
    news_items = extract_news_details(response.text)
    return news_items

@app.route('/api/update-news', methods=['GET'])
def update_news():
    try:
        page = request.args.get('page', default=1, type=int)
        news_items = fetch_and_save_news(page)
        return jsonify(news_items)
    except Exception as e:
        # Log the error for debugging
        import traceback
        print(traceback.format_exc())
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use Render's PORT environment variable
    app.run(host='0.0.0.0', port=port, debug=False)