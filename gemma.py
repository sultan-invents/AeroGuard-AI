from google import genai
from config import GEMMA_API_KEY, MODEL_NAME

client = genai.Client(
    api_key=GEMMA_API_KEY
)

def analyze_disaster(prompt, image=None):

    contents = [prompt]

    if image:
        contents.append(image)

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=contents
    )

    return response.text
