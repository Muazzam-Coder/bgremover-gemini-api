from google import genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize client
client = genai.Client(api_key=os.getenv("API-KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash-image",  # updated working model
    contents="""

You are a digital marketing expert.

Analyze this business website content and give a short audit.

Business Name: advantabyte

Website Content:
https://www.advantabyte.com/

Give output in this format:

Problems:
lack of UI

Missing Features:
Meta adds

Marketing Gaps:
didn't know about the business

Services I Can Offer:
any you can think of

    """
    )

print(response.text)