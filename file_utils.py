import json

def read_content_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_json_to_file(data, file_path):
    with open(file_path, 'w') as outfile:
        json.dump(data, outfile)

def write_markdown_to_file(markdown_content, file_path):
    with open(file_path, 'w') as file:
        file.write(markdown_content)