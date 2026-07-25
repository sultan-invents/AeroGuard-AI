from google import genai
from config import GEMMA_API_KEY


client = genai.Client(
    api_key=GEMMA_API_KEY
)


def analyze_disaster(prompt, image=None):

    models = client.models.list()

    available = []

    for model in models:
        available.append(model.name)

    return "\n".join(available)
