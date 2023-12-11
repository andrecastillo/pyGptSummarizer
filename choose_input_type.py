import sys
from video_id import get_video_id
from transcript import get_clean_transcript
from text_file import get_file_path
from process_file import get_clean_text_from_file


def make_input_choice():
    print("\nSelect input type:")
    print("1: Video ID")
    print("2: Text File")
    choice = input("Enter your choice (1 or 2): ")
    return choice


def get_input_type():
    input_type = make_input_choice()

    if input_type == '1':
        # Process for video ID
        video_id = get_video_id()
        transcript_cleaned = get_clean_transcript(video_id)
        return transcript_cleaned
    elif input_type == '2':
        # Process for text file
        file_path = get_file_path()
        processed_file = get_clean_text_from_file(file_path)
        return processed_file
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)
