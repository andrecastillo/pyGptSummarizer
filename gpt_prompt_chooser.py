import sys
import os
from file_utils import read_content_from_file

def list_prompt_files(directory):
    return tuple(os.listdir(directory))

def select_prompt_file(files):
    print("\nChoose a prompt to use:")
    for idx, file in enumerate(files, 1):
        print(f"{idx}: {file}")
    
    selection = int(input("\nSelect a prompt file (number): ")) - 1
    return files[selection] if 0 <= selection < len(files) else None

def get_prompt_content():
    # dir where the prompt files are
    prompts_dir = os.getenv('PROMPTS_DIR', 'prompts/')

    prompt_files = list_prompt_files(prompts_dir)

    selected_file = select_prompt_file(prompt_files)

    if selected_file is None:
        print("Invalid selection. Exiting.")
        sys.exit(1)

    # list the prompt files and select one
    prompt_file_path = os.path.join(prompts_dir, selected_file)

    content = read_content_from_file(prompt_file_path)
    
    return content