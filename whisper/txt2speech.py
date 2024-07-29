import openai
import config

openai.api_key =  config.OPENAI_API_KEY

speech_file = "speech.mp3"

response = openai.audio.speech.create(
	model="tts-1",
	voice="alloy",
	input="the quick brown fox jumps over the lazy dog"
)

response.stream_to_file(speech_file)


	