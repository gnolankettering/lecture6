import openai
import config

openai.api_key =  config.OPENAI_API_KEY

speech_file = "french.mp3"

response = openai.audio.speech.create(
	model="tts-1",
	voice="nova",
	input="Le rapide renard brun sauta par dessus le chien paresseux"
)

response.stream_to_file(speech_file)


	