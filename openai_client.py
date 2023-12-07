import os
import openai


def create_openai_completion(system_content, user_content, model="gpt-3.5-turbo"):

    print(f"\nPrompting model: {model}, please wait...")
    openai_api_key = os.getenv('OPENAI_API_KEY')

    # Set the API key for OpenAI
    openai.api_key = openai_api_key

    return openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_content}
        ]
    )
