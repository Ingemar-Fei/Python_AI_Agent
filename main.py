import os, sys
import dotenv
from google import genai
from google.genai import types, errors

dotenv.load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
proxy_adress = os.environ.get("PROXY_ADDRESS")
options = {
    "--verbose":False,
}

def init_proxy():
    if os.environ.get("all_proxy"):
        os.environ["all_proxy"] = ''
    if os.environ.get("ALL_PROXY"):
        os.environ["ALL_PROXY"] = ''
    os.environ["HTTP_PROXY"] = proxy_adress
    os.environ["HTTPS_PROXY"] = proxy_adress

def check_options(args):
    global  options
    for option in options:
        if option in args:
            options[option] = True
            args.remove(option)
    return args

def ask_gemini(prompt_text):
    try:
        global options
        client = genai.Client(api_key=api_key)
        messages = [
            types.Content(role="user", parts=[types.Part(text=prompt_text)])
        ]
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
        )
        print("response:",response.text)
        if options["--verbose"]:
            print(f"User prompt: {prompt_text}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    except errors.ServerError as e:
        ask_gemini(prompt_text)

if __name__ == "__main__":
    init_proxy()
    input = sys.argv
    input = check_options(input)
    if len(input) < 2:
        print("[ Error ] Please input some prompt text behind.")
        sys.exit(1)
    else:
        ask_gemini(sys.argv[1])