def get_clean_text_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
