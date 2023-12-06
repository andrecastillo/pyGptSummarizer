import json

def convert_to_json(message):

    # Remove the Markdown code block notation
    if message.startswith("```json") and message.endswith("```"):
        json_string = message[7:-3].strip()  # Extract the JSON string

        # Parse the JSON string into a Python dictionary
        return json.loads(json_string)
    else:
        # Handle cases where the message is not in the expected format
        return json.loads(message)