from img2txt.img2txt import img2txt
from txt2aud.txt2aud import txt2aud
from scipy.io.wavfile import write
from gpt import askgpt

if __name__ == '__main__':

    imgdir = input("Please pass me a file path of image : ")

    text = img2txt(imgdir)

    text_improved = askgpt(text)

    audio = txt2aud(text_improved)

    write("outputs/output.wav", rate=16000, data=audio)

    print(f"Audio about \n\"\n{text_improved}\n\"\nsuccessfully generated.")
