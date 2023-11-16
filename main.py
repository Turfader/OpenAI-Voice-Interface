import dotenv
import openai
from openai import OpenAI
import os
from text_to_speech import read

dotenv.load_dotenv()
api_key = os.getenv("API_KEY")

client = OpenAI(api_key=api_key)

while True:
    #user_input = input("Ask the AI something: ")
    user_input = 'This is a test. Please say "Hello world"'
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are an AI assistant, used for testing code"},
        {"role": "user", "content": user_input}
      ]
    )

    print(completion.choices[0].message)
    read(str(completion.choices[0].message.content))
    break
