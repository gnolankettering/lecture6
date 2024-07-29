import base64
from openai import OpenAI
import config
client = OpenAI(api_key=config.OPENAI_API_KEY)

# response = client.images.generate(
#   model="dall-e-2",
#   prompt="a white siamese cat",
#   size="256x256",
#   quality="hd",
#   n=1,
#   response_format="b64_json"
# )
response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="hd",
  n=1,
  response_format="b64_json"
)

img_data = response.data[0].b64_json.encode()

with open("imageToSave.png", "wb") as fh:
   fh.write(base64.decodebytes(img_data))
    

