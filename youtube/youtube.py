from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi

import config
import json

client = OpenAI(api_key=config.OPENAI_API_KEY)

# Download the transcript from the YouTube video
transcript_list = YouTubeTranscriptApi.list_transcripts('r5gjUZisWNE')
transcript = transcript_list.find_generated_transcript(['en']).fetch()

# Extract and concatenate all text elements
concatenated_text = " ".join(item['text'] for item in transcript)
print(concatenated_text)

# file is going to be too long so we need to split it into smaller chunks
def split_string_into_chunks(input_string, chunk_size=4096):
    return [input_string[i:i + chunk_size] for i in range(0, len(input_string), chunk_size)]

# Example usage
chunks = split_string_into_chunks(concatenated_text)

# Printing the chunks to verify
for i, chunk in enumerate(chunks):
    response = client.audio.speech.create(
    	model="tts-1",
	    voice="alloy",
	    input=chunk
    )
    response.stream_to_file(f"speech_{i}.mp3")



