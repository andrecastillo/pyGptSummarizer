# pyGptSummarizer 

Thanks to Daniel Miessler of Unsupervised Learning for the idea to make this. He had already done the hard work of making the great prompt, and using the YouTubeAPI transcript library to pull transcripts from YouTube videos.

He makes great content, I'm a subscriber, and member, and you should be too.

https://danielmiessler.com/

All I did was piggyback off the idea to turn the response into Markdown, and let myself choose from a couple different but similar prompts for different areas of thought, and then built some more functionality in and around that.

# Description
It's a fairly rudimentary python program that allows you to send a very specific prompt to the OpenAI API, along with a transcript from a YouTube Video, or a text file, in order to get a summary of the important parts and ideas of the video in the form of a markdown file. 

While there are tools that do something similar, this one works exactly how I want and expect it to. I've tailored to work specifically with Obsidian. It uses tags the way Obsidian uses them, and my extract path is directly into a local Obsidian vault (which of course you can change). 

# Installation and Setup

`pip install -r requirements.txt`

Make a copy then rename `.env-example` file `.env`

Go into `.env` and add the OpenAI Secret Key, and add the path where you want summaries extracted to. 

Lastly, you're going to need at least one prompt file in the `prompts/` directory. There's a file `example_prompt.txt` in the root of the project. Copy it and rename it to whatever you want and put it in the `prompts/` directory. Go into the new file and update it per the instructions.

# Usage

From the root of the project, after you've put in all the necessary values into your local .env file, just run 
`python main.py`

Or If you are in Ubuntu.

`python3 main.py`

You'll be prompted to choose a model. GPT-4 is the most expensive one right now. So if you want to just see how it works, go with a GPT 3.5 variant. 

Then you'll be prompted to choose a prompt. The list will show all prompts that exist in the `prompts/` directory.

Lastly it'll ask you if you want to give it a video to summarize or a file. If you choose Video, it'll ask you for the YouTube Video ID, if you choose file, it'll ask you for the path to the text file.

After that, it'll run, and you'll get your results wherever you set your extraction path to.

Have Fun!

## Additional Help

https://platform.openai.com/docs/quickstart?context=python

You should check out the Open AI API Quick Start instructions, linked above, first if you haven't already been using the OpenAI API as you'll need to get the API Secret Key and have it as one of your environment variables. When reviewing the instructions, don't worry about putting the key into your local environment (bash or whatever), as you'll be putting the key into the .env file in the root of your project.



You'll need the OpenAI python library to make the API calls, again, if you followed the quickstart instructions it'll get you that. 

You'll also need to install the youtube-transcript-api: see link for details and installation instructions https://pypi.org/project/youtube-transcript-api/ 

There's a requirements.txt file, so you can install all the dependencies, including the ones named above. So, probably best to just use that.

You'll need to create a prompt text file that goes in the prompts folder. I've created an example prompt file located in the root of the project called example_prompt, and it'll explain how you should structure your prompt for it to work with this code. You can create multiple prompts using a different text file per prompt, just keep the same format or adjust the code I guess if you wanted.  