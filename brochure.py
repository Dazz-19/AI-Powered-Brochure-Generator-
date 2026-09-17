from playwright.sync_api import sync_playwright
import gradio as gr
from scraper import get_page_text,get_relevant_links
from config import gemini
import os


def create_brochure(website_link, word_limit):
    progress = gr.Progress()

    progress(0.2, desc="Finding website links...")
    web_links = get_relevant_links(website_link)

    progress(0.5, desc="Reading website content...")

    all_con = ""
    for i in web_links:
        con = get_page_text(i)
        all_con += con

    b_system_prompt = """You are an expert brochure designer known for creating vibrant, eye-catching HTML brochures 
that people actually want to read.

Design rules you always follow:
- Use plenty of emojis throughout — in headings, section titles, bullet points, and CTAs
- Create a bold, colorful hero section with a large emoji as the brand icon
- Use gradient backgrounds on sections (CSS linear-gradient works in PDF)
- Add colored cards with subtle box-shadows and rounded corners (border-radius: 12px)
- Use a vibrant 4-5 color palette — don't be afraid of bold colors
- Use Unicode symbols and emojis as bullet points instead of plain dots
- Keep text concise and punchy — short phrases over long paragraphs
- Use inline CSS only — no external stylesheets, no JavaScript
- Avoid flexbox and CSS grid — use table-based or float-based layouts for PDF compatibility
- Include: hero header, about, features/offerings (as emoji cards), fun facts or stats, and a CTA footer
- Add a stats/numbers section like "🌍 50+ Countries  👥 10,000+ Users  ⭐ 4.9 Rating"
- Make headings large and colorful with emoji prefixes

Tone: fun, energetic, and memorable — like a startup pitch deck meets a festival poster."""

    b_user_prompt = f"""
Create a FUN and visually exciting brochure using the content below.

Content:
{all_con[:5000]}

Requirements:
- Approximately {word_limit} words
- Use LOTS of emojis in headings, lists, and throughout the text
- Bright, bold color scheme
- Cards with colored backgrounds for each section
- A stats/numbers row with emoji icons
- Gradient hero section
- Make it feel exciting and modern, not corporate and boring
- Return ONLY the raw HTML, no markdown fences

"""
    progress(0.8, desc="Generating brochure...")

    b_response = gemini.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "system", "content": b_system_prompt},
            {"role": "user", "content": b_user_prompt}]
    )
    html = b_response.choices[0].message.content
    html = html.replace("```html", "")
    html = html.replace("```", "")
    html = html.strip()

    with open("brochure.html", "w") as f:
        f.write(html)

    html_path = os.path.abspath("brochure.html")
    pdf_path = os.path.abspath("brochure.pdf")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file://{html_path}")
        page.pdf(path=pdf_path, format="A4")
        browser.close()
    progress(0.9, desc="📑 Creating PDF...")

    progress(1.0, desc="✅ Done!")
    return html, html_path, pdf_path