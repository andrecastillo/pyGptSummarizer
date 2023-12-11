import os
import json
from dotenv import load_dotenv
from model_chooser import choose_gpt_model
from gpt_prompt_chooser import get_prompt_content
from choose_input_type import get_input_type
from openai_client import create_openai_completion
from response_prep import get_cleaned_response
from markdown_converter import convert_to_markdown
from file_utils import write_markdown_to_file

# get the environment information needed
load_dotenv()

# set the model var for use in the OpenAI API call
model = choose_gpt_model()

# read the prompt they chose into memory
system_prompt_content = get_prompt_content()

# get the user prompt content, either a video transcript or a text file
user_prompt_content = get_input_type()

# call openai api
completion = create_openai_completion(system_prompt_content, user_prompt_content, model)
print(f"\nResponse received...")

# save raw response before cleaning
raw_response_path = os.getenv('RAW_RESPONSE_PATH', 'output/')
with open(f"{raw_response_path}{completion['id']}", 'w') as raw_file:
    json.dump(completion, raw_file, indent=4)

# do the work of cleaning and preparing the response, turning into dict, etc
response = get_cleaned_response(completion, model)

# do the markdown stuff and write the file
markdown, sanitized_title = convert_to_markdown(response)
extraction_path = os.getenv('EXTRACTION_PATH', 'extractions/')
output_md_path = f"{extraction_path}{sanitized_title}.md"
write_markdown_to_file(markdown, output_md_path)
print(f"\nFile \"{sanitized_title}\" written.")

# all done
print("\nProcessing complete.\n")
