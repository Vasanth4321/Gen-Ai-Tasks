import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found")

client = genai.Client(api_key=API_KEY)

SYSTEM_PROMPT = """
You are a Blog Assistant.

Role:
- Help users write blogs.
- Generate SEO-friendly content.
- Improve readability and engagement.

Constraints:
- Stay focused on blogging.
- Give concise and practical responses.
"""

def get_response(user_input: str) -> str:
    try:
        prompt = f"""
        {SYSTEM_PROMPT}

        User Query:
        {user_input}
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )


        return response.text

    except Exception as e:
        print("ERROR:", e)
        return f"Error: {str(e)}"