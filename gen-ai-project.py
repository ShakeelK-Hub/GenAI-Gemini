import google.generativeai as genai

API_KEY = \
"AIzaSyBnpeaUX1H-wYMowzkd91CtGdwVWLNa-so"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')
chat = model.start_chat()

while True:
    userInput = input("You: ")
    if userInput.lower() == "exit":
        break
    response = chat.send_message(userInput)
    print("Gemini: ", response.text)