import re

def sanitize_title(title):
    # Replace special characters with a space
    sanitized = re.sub(r'[^\w\s-]', ' ', title)
    # Replace multiple spaces with a single space
    sanitized = re.sub(r'\s+', ' ', sanitized)
    return sanitized.strip()

def convert_to_markdown(data):
    markdown_content = ""
    sanitized_title = ""

    if 'TITLE' in data['message']:
        sanitized_title = sanitize_title(data['message']['TITLE'])
        markdown_content += f"# {sanitized_title}\n\n"
    if 'SUMMARY' in data['message']:
        markdown_content += f"## SUMMARY\n"
        markdown_content += f"{data['message']['SUMMARY']}\n\n"

    # Adding other sections
    for key in data['message']:
        if key == 'TITLE' or key == 'SUMMARY':
            continue  # Skip the title and summary as they're already added

        if key == 'TAGS':
            # handle tags section
            markdown_content += f"## {key}\n"
            tags = ' '.join(f"#{tag}" for tag in data['message'][key])  # Format tags for Obsidian
            markdown_content += tags + "\n\n"
        else:
            markdown_content += f"## {key}\n"
            if isinstance(data['message'][key], list):
                for item in data['message'][key]:
                    markdown_content += f"- {item}\n"
            else:
                markdown_content += f"{data['message'][key]}\n"
            markdown_content += "\n"

    markdown_content += "## Additional Info\n"

    markdown_content += "### Response Details\n"
    markdown_content += f"- **Model:** {data['model']}\n"
    markdown_content += f"- **Created:** {data['created']}\n"
    markdown_content += f"- **ID:** {data['id']}\n"
    markdown_content += f"- **Role:** {data['role']}\n"
    markdown_content += f"- **Finish Reason:** {data['finish_reason']}\n"
    markdown_content += "\n"
    markdown_content += "### Usage Details\n"
    markdown_content += f"- **Completion Tokens:** {data['usage_completion_tokens']}\n"
    markdown_content += f"- **Prompt Tokens:** {data['usage_prompt_tokens']}\n"
    markdown_content += f"- **Total Tokens:** {data['usage_total_tokens']}\n"

    return markdown_content, sanitized_title