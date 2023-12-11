import sys
from youtube_transcript_api import YouTubeTranscriptApi


def get_clean_transcript(video_id):
    print("\nRetrieving transcript...")
    transcript_data = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'en-GB'])
    cleaned = ' '.join(segment['text'] for segment in transcript_data) 
    print("\nTranscript retreived and cleaned...")
    return cleaned


# If I need to test just this script
if __name__ == "__main__":

    # get video id from command line argument
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <video_id>")
        sys.exit(1)

    # Example video_id for testing
    test_video_id = sys.argv[1]

    # Fetch and print the transcript
    print(get_clean_transcript(test_video_id))
