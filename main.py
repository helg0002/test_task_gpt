from openai import OpenAI
from docx import Document
from io import BytesIO
import requests
from cfg import config

client = OpenAI(
  api_key=config.creds.key
)

public_url = config.creds.url
api_url = "https://cloud-api.yandex.net/v1/disk/public/resources/download"
params = {"public_key": public_url}

response = requests.get(api_url, params=params)
download_url = response.json()["href"]

file_bytes = requests.get(download_url).content

doc = Document(BytesIO(file_bytes))

check = 0
with open("prompts.txt", "a", encoding="utf-8") as f:
    for p in doc.paragraphs:
        if check == 5:
            break
        response = client.responses.create(
            model="gpt-5-nano",
            input=f"You are a film director, anthropologist, and visual historian creating cinematic video prompts for Google Veo 3 (fast mode). Your task is to generate 1 prompt in English from the provided paragraph of a prehistoric narrative script.\n\nparagraph = {p.text}",
            store=True,
        )
        answer_text = response.output[1].content[0].text
        f.write(f"Request: {p.text}\n")
        check += 1
        f.write(f"Answer: {answer_text}\n\n")

