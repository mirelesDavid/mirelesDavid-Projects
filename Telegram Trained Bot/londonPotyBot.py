import openai
import requests
import time

openai.api_key = "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"
TOKEN = "6173563065:AAG5x_gKZBZI0nBatuCSvA45QNRE7UsJ1Fg"

def get_updates(token, offset=None):
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    params = {"timeout": 100, "offset": offset}  # Corrección aquí
    response = requests.get(url, params=params)
    return response.json()["result"]

def send_messages(chat_id, text):  # Corrección aquí
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"  # Corrección aquí
    params = {"chat_id": chat_id, "text": text}
    response = requests.post(url, params=params)
    return response

def get_openai_response(prompt):
    model_engine = "babbage:ft-personal-2023-09-24-10-23-34"  # Asegúrate de tener un motor válido aquí
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,  # Corrección aquí
        max_tokens=200,
        n=1,
        stop= None,
        temperature=0.5  # Corrección aquí
    )
    return response.choices[0].text.strip()

def main():
    print("Starting bot..")
    offset = 0
    while True:
        updates = get_updates(TOKEN, offset)  # Corrección aquí
        if updates:
            for update in updates:
                offset = update["update_id"] + 1
                chat_id = update["message"]["chat"]["id"]  # Corrección aquí
                user_message = update["message"]["text"]
                print(f"Received message: {user_message}")
                GPT = get_openai_response(user_message)
                send_messages(chat_id, GPT)
        else:
            time.sleep(1)

if __name__ == '__main__':
    main()
