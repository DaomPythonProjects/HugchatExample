import dotenv
from hugchat import hugchat
from hugchat.login import Login
from dotenv import load_dotenv
import os


def login_hugchat():
    load_dotenv()
    sign = Login(os.getenv("EMAIL"), os.getenv("PASSWORD"))
    cookies = sign.login()
    chatbot = hugchat.ChatBot(cookies=cookies)
    return chatbot


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    chatbot = login_hugchat()
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    chatbot.switch_llm(1)
    print("Hola...")
    while True:
        user_input = input('> ')
        print(chatbot.chat(user_input))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
