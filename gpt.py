import os
import openai


#Open API key
openai.api_key = "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"

#GPT에게 물어볼 질문
question = "Desccribe the sound of " + input("What to ask?") + "in a sentence, without visual expression and emphasize on audio expression."

#GPT에게 질문
completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages= [
        {"role": "user", "content": question}
    ]
)

print(completion.choices[0].message.content)