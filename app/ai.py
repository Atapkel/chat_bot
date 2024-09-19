import google.generativeai as genai
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

genai.configure(api_key=os.getenv('API_AI'))
model = genai.GenerativeModel("gemini-1.5-flash")


async def get_response(request: str):
   response = await asyncio.to_thread(model.generate_content, request)
   return response.text


