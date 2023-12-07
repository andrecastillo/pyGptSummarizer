import datetime
from convert_to_json import convert_to_json


def get_cleaned_response(completion, model):

    # seems like there's a difference in the way the models respond
    # the message part with gpt4 has some extra json formatting of some kind, not sure
    # what to call it, but I clean it up if using gpt4 model, and don't clean it up if using
    # the gpt3 model. Could be that different models respond even more differently, so
    # I may have to handle that at some point in the future
    if model == "gpt-4-1106-preview":
        message = convert_to_json(completion.choices[0].message.content)
    else:
        orig_message = completion.choices[0].message.content
        cleaned_up = orig_message.replace('\n', '')
        message = convert_to_json(cleaned_up)

    # build gpt response into dict
    return {
        "id": completion.id,
        "role": completion.choices[0].message.role,
        "message": message,
        "finish_reason": completion.choices[0].finish_reason,
        "created_epoch": completion.created,
        "created": datetime.datetime.fromtimestamp(completion.created).strftime('%Y-%m-%d %H:%M:%S'),
        "model": completion.model,
        "usage_completion_tokens": completion.usage.completion_tokens,
        "usage_prompt_tokens": completion.usage.prompt_tokens,
        "usage_total_tokens": completion.usage.total_tokens,
    }
