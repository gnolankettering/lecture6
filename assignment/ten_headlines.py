# give me 10 headlnes, in JSON format, divide labor by telling it to do the headlines step by step
from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_API_KEY)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    # Conversation as a list of messages.
    messages=[
        {"role": "system", "content": "You are the famous American film critics and television partners Siskel and Ebert. Output the review in JSON format.\
                    Do the headlines step by step"},
        {
            "role": "user",
            "content": "Please write a movie review for the Godfather in the style of Siskel and Ebert in 15 words",
        },
        {
            "role": "assistant",
            "content": "A masterful blend of compelling storytelling, rich character depth, and unforgettable performances - two thumbs up!",
        },
        {"role": "user", "content": "Please write 10 headlines for a movie review for the movie Up! in the style of Siskel and Ebert in 15 words in JSON format"},
    ]
)

print(response.choices[0].message.content)