import requests
from bs4 import BeautifulSoup
import json
from config import gemini


def get_relevant_links(url):
    res = requests.get(url, timeout=10)
    soup = BeautifulSoup(res.text, "html.parser")

    all_links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        # Convert relative links to absolute
        if href.startswith("/"):
            href = url.rstrip("/") + href
        if href.startswith("http"):
            all_links.append(href)

    all_links = list(set(all_links))

    system_prompt = """You are given a website url , you need to pick put the relevant links that might be useful to create a company brocheure.\
    leave out links like privacy ,mail me etc   give all the results in this  JSON format

   {
    "links": [
        {"type": "about page", "url": "https://full.url/goes/here/about"},
        {"type": "careers page","url": "https://another.full.url/careers"}
    ]
   }
    """

    user_prompt = f"Filter these links:\n{json.dumps(all_links)}"
    response = gemini.chat.completions.create(
        model='gemini-2.5-flash',
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        response_format={"type": "json_object"}
    )

    text = response.choices[0].message.content
    final_links = json.loads(text)

    to_scrape_links = []
    data = final_links["links"]
    for d in data:
        to_scrape_links.append(d["url"])
    return to_scrape_links




def get_page_text(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    contents = soup.get_text()
    return contents
