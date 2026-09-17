# 🚀 AI Brochure Generator

An AI-powered web application that generates beautiful, colorful brochures from any company website.

Simply enter a company URL, and the application automatically:

- 🌐 Scrapes the website
- 🤖 Identifies the most relevant pages using Google Gemini
- 📝 Extracts important content
- 🎨 Designs an attractive HTML brochure
- 📄 Exports the brochure as both HTML and PDF

Built with **Python**, **Gradio**, **Google Gemini**, **BeautifulSoup**, and **Playwright**.

---

# ✨ Features

- 🌍 Generate brochures from any company website
- 🤖 AI-powered link filtering
- 📑 Multi-page website content extraction
- 🎨 Beautiful HTML brochure generation
- 📄 PDF export
- 🎛 Adjustable brochure length using a slider
- 📊 Live progress updates while generating
- 💻 Interactive Gradio interface

---

# 🛠 Tech Stack

- Python
- Gradio
- Google Gemini API
- OpenAI Python SDK
- BeautifulSoup4
- Requests
- Playwright
- python-dotenv

---

# 📂 Project Structure

```
ai-brochure-generator/
│
├── app.py
├── brochure.py
├── scraper.py
├── config.py
│
├── assets/
│
├── README.md
├── requirements.txt
├── .gitignore
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-brochure-generator.git
cd ai-brochure-generator
```

---

## 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it

### macOS/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Playwright

```bash
playwright install
```

---

## 5. Create a `.env` file

```text
GEMINI_API_KEY=your_api_key_here
```

---

## 6. Run the application

```bash
python app.py
```

---

# 📸 Screenshots

## Home Page

> *(Add a screenshot here)*

---

## Generated Brochure

> *(Add another screenshot here)*

---

# 💡 How It Works

1. User enters a website URL.
2. Website links are collected using BeautifulSoup.
3. Google Gemini filters the most relevant pages.
4. The application scrapes useful content.
5. Gemini generates a colorful HTML brochure.
6. Playwright converts the HTML into a PDF.
7. The brochure is available for download.

---

# 🚀 Future Improvements

- Company logo extraction
- Dark mode
- Multiple brochure themes
- Custom color palettes
- Multi-language brochures
- Image generation support
- One-click deployment

---

# 👩‍💻 Author

**Dhanushree H M**

If you enjoyed this project, feel free to ⭐ the repository!
