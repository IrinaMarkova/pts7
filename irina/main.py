import os
from tkinter import *
from KandynskyAPI import *
import base64
root = Tk()
root.geometry('490x60+830+520')
root.title('AI Image')
icon = PhotoImage(file='3480109.png')
root.iconphoto(True, icon)
root.resizable(False, False)
root.config(background='black')

entry = Entry()
entry.place(x=10, y=10, width=450, height=35)

def click():
    if __name__ == '__main__':
        api = Text2ImageAPI('https://api-key.fusionbrain.ai/', '76A96B7FA5CFDAA74BD10E6E2508557E',
                            '7FEA56A0882D80EBA4819D6A423A790D')
        model_id = api.get_model()
        uuid = api.generate(entry.get(), model_id)
        images = api.check_generation(uuid)

        base64_img = str(images)
        img_bytes = base64_img.encode('utf-8')
        with open('image.png', 'wb') as file:
            decode = base64.decodebytes(img_bytes)
            file.write(decode)
        os.startfile('image.png')


btn_icon = PhotoImage(file='send.png')
btn = Button(image=btn_icon,
           command=click)
btn.place(x=450, y=15, width=30, height=30)

root.mainloop()
