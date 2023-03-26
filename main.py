import openai

# Configura a API key do OpenAI
openai.api_key = "####"

# Cria uma lista vazia para armazenar as mensagens do chatbot
messages = []

# Pede ao usuário que tipo de chatbot ele deseja criar
system_msg = input("Que tipo de chatbot você quer criar?\n")
messages.append({"role": "system", "content": system_msg})

print("Seu novo assistente está pronto!")

# Loop principal do chatbot
while input != "quit()":
    # Lê a mensagem do usuário
    message = input()
    messages.append({"role": "user", "content": message})

    # Envia a mensagem para o modelo de chat do OpenAI
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="\n".join([m["content"] for m in messages]),
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extrai a resposta gerada pelo modelo de chat
    reply = response.choices[0].text.strip()
    messages.append({"role": "assistant", "content": reply})

    # Imprime a resposta do chatbot
    print("\n" + reply + "\n")
