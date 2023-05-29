import openai

def askgpt(result):
    openai.api_key = input("Paste your openai API_key")
    feature = result[0]
    place = result[1]
    weather = result[2]

    # GPT에게 물어볼 질문
    question = "Desccribe the atmosphere of " + feature + "in" + place + "on" + weather + "day, emphasizing on audio expression."

    # GPT에게 질문
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question}
        ]
    )

    return (completion.choices[0].message.content)
