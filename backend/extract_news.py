import json
from bs4 import BeautifulSoup

def extract_news_details(response_text):
    data = json.loads(response_text)
    # Find the object with the 'viewsShowMore' command
    html_data = None
    for obj in data:
        if obj.get("command") == "viewsShowMore":
            html_data = obj.get("data")
            break
    if not html_data:
        print("No news data found in response.")
        return []

    # Parse the HTML
    soup = BeautifulSoup(html_data, "html.parser")
    news_cards = soup.find_all("div", class_="card position-relative horizontal type-horizontal-list row border-bottom collapse image-reverse")

    news_list = []
    for card in news_cards:
        # Headline and news URL
        title_tag = card.find("h3", class_="title")
        if title_tag and title_tag.a:
            headline = title_tag.a.get_text(strip=True)
            news_url = "https://www.thedailystar.net" + title_tag.a["href"]
        else:
            headline = news_url = None

        # Short description
        intro_tag = card.find("p", class_="intro")
        description = intro_tag.get_text(strip=True) if intro_tag else None

        # Image URL
        img_tag = card.find("img", class_="ratio ratio__16x9 lazyload")
        if img_tag:
            image_url = img_tag.get("data-srcset") or img_tag.get("data-src")
        else:
            image_url = None

        news_list.append({
            "headline": headline,
            "description": description,
            "image_url": image_url,
            "news_url": news_url
        })

    return news_list

# Example usage:
if __name__ == "__main__":
    # Read the response text from a file or variable
    with open("response.txt", "r", encoding="utf-8") as f:
        response_text = f.read()
    news_items = extract_news_details(response_text)
    for news in news_items:
        print(news)