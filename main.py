import os
import json
from dotenv import load_dotenv
from video_id import get_video_id
from transcript import get_clean_transcript
from model_chooser import choose_gpt_model
from gpt_prompt_chooser import get_prompt_content
from openai_client import create_openai_completion
from response_prep import get_cleaned_response
from markdown_converter import convert_to_markdown
from file_utils import write_markdown_to_file

# get the environment information needed
load_dotenv()

# get video id from input command
video_id = get_video_id()

# get transcript and clean it
transcript_cleaned = get_clean_transcript(video_id)

# set the model var for use in the OpenAI API call
model = choose_gpt_model()

# read the prompt they chose into memory
gpt_prompt = get_prompt_content()

# call openai api
completion = create_openai_completion(gpt_prompt, transcript_cleaned, model)
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
