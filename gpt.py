import openai
from img2txt.img2txt import img2txt

#Open API key
openai.api_key = "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"

# if __name__=='__main__':
#     #이미지 파일 주소 받기
#     imgdir = input("Please pass me a file path of image : ")
#
#     #img2txt 변환
#     result = img2txt(imgdir)
#     feature = result[0]
#     place = result[1]
#     weather = result[2]
#
#     #GPT에게 물어볼 질문
#     question = "Desccribe the atmosphere of " + feature + "in" + weather + place + "emphasizing on audio expression."
#
#     #GPT에게 질문
#     completion = openai.ChatCompletion.create(
#             model = "gpt-3.5-turbo",
#             messages= [
#                 {"role": "user", "content": question}
#             ]
#         )
#
#     print(completion.choices[0].message.content)

def askgpt():
    # 이미지 파일 주소 받기
    imgdir = input("Please pass me a file path of image : ")

    # img2txt 변환
    result = img2txt(imgdir)
    feature = result[0]
    place = result[1]
    weather = result[2]

    # GPT에게 물어볼 질문
    question = "Desccribe the atmosphere of " + feature + "in" + weather + place + "emphasizing on audio expression."

    # GPT에게 질문
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question}
        ]
    )

    return (completion.choices[0].message.content)