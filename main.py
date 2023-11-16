import dotenv
from openai import OpenAI
from text_to_speech import read
from speech_to_text import transcribe_microphone

dotenv.load_dotenv()
client = OpenAI()

while True:
    # user_input = input("Ask the AI something: ")
    # user_input = 'This is a test. Please say "Hello world"'
    user_input = transcribe_microphone()
    if user_input == "stop":
        break
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are an AI assistant, used for testing code. The user input"
                                      "will be from voice recognition. Please use logic to deduce what is"
                                      "being said. In the event of confusion, please ask the user to repeat"},
        {"role": "user", "content": user_input}
      ]
    )

    print(completion.choices[0].message)
    read(str(completion.choices[0].message.content))
    # break
