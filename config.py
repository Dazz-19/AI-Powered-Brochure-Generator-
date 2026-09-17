# Imports

import os
from dotenv import load_dotenv
from openai import OpenAI



load_dotenv(override=True)
gemini_api_key = os.getenv('GEMINI_API_KEY')

if gemini_api_key:
    print("Gemini API Key exists")
else:
    print("Google API Key not set ")



gemini=OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/openai/",api_key=gemini_api_key)


