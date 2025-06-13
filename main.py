import os
import dotenv
from google import genai

dotenv.load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
proxy_adress = os.environ.get("PROXY_ADDRESS")
print(proxy_adress)
os.system('unset all_proxy')
os.system('unset ALL_PROXY')
os.environ["HTTP_PROXY"] = proxy_adress
os.environ["HTTPS_PROXY"] = proxy_adress
client = genai.Client(api_key=api_key)
promt_word = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=promt_word,
)
print("response:",response.text)
print("Prompt tokens:",response.usage_metadata.prompt_token_count)
print("Response tokens:",response.usage_metadata.candidates_token_count)
