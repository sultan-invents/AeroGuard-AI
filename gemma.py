from google import genai
from PIL import Image

from config import GEMMA_API_KEY


client = genai.Client(
    api_key=GEMMA_API_KEY
)


def analyze_disaster(prompt, image=None):

    contents = [prompt]

    if image:
        img = Image.open(image)
        contents.append(img)

    response = client.models.generate_content(
        model="gemma-4-31b-it",
        contents=contents
    )

    return response.text
