import json
import requests
import random
from io import BytesIO
from PIL import Image, ImageTk
import tkinter as tk

# Работа с OpenWeatherMap
DIFFERENCE = 273.15

city_name = 'London'
key = 'f08a82a65811df98d10a99c13ed60d6f'
responseMap = requests.post(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}')
resultMap = json.loads(responseMap.text)
print(f"The weather in {resultMap['name']} now: {round(resultMap['main']['temp'] - DIFFERENCE, 2)}°C, влажность {resultMap['main']['humidity']}%, давление составляет {resultMap['main']['pressure']} мм рт.ст.")

#Работа с rickandmortyapi.com
while True:
    inf = input("Введите какую информацию вы хотите получиить о Рике и Морти: 1 - информация о персонажах мультсериала, 2 - информация о местоположениях в мультсериале, 3 - информация об эпизодах, 0 - выход: ")
    match inf:
        case "1":
            id = input("Введите id персанажа (от 1 до 826 вкл): ")
            response = requests.get(f"https://rickandmortyapi.com/api/character/{id}")
            text = json.loads(response.text)
            print(f"Информация о персонаже {text['name']}:\n статус {text['status']}, вид {text['species']}, пол {text['gender']}, происхождение {text['origin']['name']}, расположение {text['location']['name']}\n")
        case "2":
            id = input("Введите id местоположения (от 1 до 126 вкл): ")
            response = requests.get(f"https://rickandmortyapi.com/api/location/{id}")
            text = json.loads(response.text)
            print(f"Информация о месте {text['name']}:\n тип {text['type']}, измерение {text['dimension']}\n")
        case "3":
            id = input("Введите номер эпизода (от 1 до 51 вкл): ")
            response = requests.get(f"https://rickandmortyapi.com/api/episode/{id}")
            text = json.loads(response.text)
            print(f"Информация об эпизоде №{text["id"]}:\n название {text['name']}, дата выхода {text['air_date']}\n")
        case "0":
            break
        case _:
            print("Мне бы чиселки 0, 1, 2 или 3...")

# Работа с randomfox.ca
COUNT_FOX = 123

def get_fox():
    number= random.randint(1, COUNT_FOX)
    responseFox = requests.get(f'https://randomfox.ca/images/{number}.jpg')
    image_data = Image.open(BytesIO(responseFox.content))
    img = ImageTk.PhotoImage(image_data)

    lbl_img.config(image=img)
    lbl_img.image = img

    wind_width = img.width()
    wind_height = img.height()
    window.geometry(f"{wind_width}x{wind_height}")


window = tk.Tk()
window.title("Random Fox")
window.geometry("300x300")

lbl_img = tk.Label(window)
lbl_img.pack()

btn = tk.Button(window, text="Next fox", command=get_fox)
btn.place(x=10, y=10)

window.mainloop()