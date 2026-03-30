from google import genai

# Initialize client
client = genai.Client(api_key="AIzaSyDNcFMK6PwY_6OUXj49ML5460SGQGosA70")

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