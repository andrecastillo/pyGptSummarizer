import sys

def get_video_id():
    # get video id from command line argument
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <video_id>")
        sys.exit(1)

    return sys.argv[1]