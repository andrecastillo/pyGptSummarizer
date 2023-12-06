# py-wisdom-extractor 

## Description
It's a python program that allows you to send a very specific prompt to the OpenAI API, along with a transcript from a YouTube Video, in order to get a summary of the important parts and ideas of the video in the form of a markdown file. 

Personally I've tailored it a bit to work specifically with obsidian. It uses tags the way obsidian uses them, and my extract path is directly into my local obsidian.   

## Installation
https://platform.openai.com/docs/quickstart?context=python

You should check out the Open AI API Quick Start instructions, linked above, first if you haven't already been using the OpenAI API as you'll need to get the API Secret Key and have it as one of your environment variables. When reviewing the instructions, don't worry about putting the key into your local environment (bash or whatever), as you'll be putting the key into the .env file in the root of your project.

You'll need the OpenAI python library to make the API calls, again, if you followed the quickstart instructions it'll get you that. 

You'll also need to install the youtube-transcript-api: see link for details and installation instructions https://pypi.org/project/youtube-transcript-api/ 

You'll need to create a prompt text file that goes in the prompts folder. I've created an example prompt file located in the root of the project called example_prompt, and it'll explain how you should structure your prompt for it to work with this code. You can create multiple prompts using a different text file per prompt, just keep the same format or adjust the code I guess if you wanted.  

Lastly, copy the .env-example file and then rename it to just .env, and then update all the values as necessary. If you have additional GPT models you want to use, add them in your .env file or the example file before you copy and rename it.

## Usage
From the root of the project, after you've put in all the necessary values into your local .env file, just run 
`python main.py {youtube_video_id}`

OR

`python3 main.py {youtube_video_id}`

If you are in Ubuntu.

You'll be prompted to choose a model, and then you'll be prompted to choose a prompt. After that, it'll run and the output when complete will show up in wherever you told it to.

Have Fun!