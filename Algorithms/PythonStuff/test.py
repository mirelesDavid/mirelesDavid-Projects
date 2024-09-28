import openai
openai.api_key = '-'  # Reemplaza con tu clave de API real
openai.api_base = 'http://198.145.126.109/v1'  # Usando la IP que te proporcionaron

response = openai.ChatCompletion.create(
    model="tgi",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ],
    stream=False
)

print(response)
