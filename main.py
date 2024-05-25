import tkinter
from tkinter import *
from tkinter import ttk
from geopy.exc import GeocoderUnavailable
from geopy.geocoders import Nominatim
import pytz
import datetime
from timezonefinder import TimezoneFinder
place = ""

root = Tk()  # создаем корневой объект - окно
root.title("Время в любой точке мира")  # устанавливаем заголовок окна
root.geometry("300x500")  # устанавливаем размеры окна

label1 = Label(text="С помощью данного приложения ")  # создаем текстовую метку
label2 = Label(text="Вы можете определить  время")  # создаем текстовую метку
label3 = Label(text="и координаты любого города мира!")  # создаем текстовую метку
label1.pack()  # размещаем метку в окне
label2.pack()  # размещаем метку в окне
label3.pack()  # размещаем метку в окне

label4 = Label(text="Введите город: ")  # создаем текстовую метку
label4.pack(anchor="nw", padx=20, pady=30)

entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)

# получаем координаты по названию

def location():
    geolocator = Nominatim(user_agent="Tester")
    try:
#    adress = str(input('Введите город: \n')) #Получаем интересующий нас адрес
        adress = entry.get() #Получаем интересующий нас адрес
        location = geolocator.geocode(adress)
        print('Координаты места: ')
        label6 = Label(text="Координаты места: ")  # создаем текстовую метку
        label6.pack()  # размещаем метку в окне
        print(location.latitude, location.longitude)
        label7 = Label(text=(location.latitude, location.longitude))  # создаем текстовую метку
        label7.pack()  # размещаем метку в окне

    except:     # обработка несуществующего города
        label6 = Label(text="Неизвестный город")  # создаем текстовую метку
        label6.pack()  # размещаем метку в окне
        print("Неизвестный город")
        #exit ()

    # определить время по координатам

    tf = TimezoneFinder(in_memory=True)
    longitude = location.longitude  #
    latitude = location.latitude
    timezone = tf.timezone_at(lng=longitude, lat=latitude)
    now = datetime.datetime.now(pytz.timezone(timezone))
    label8 = Label(text="Часовой пояс и текущее время: ")  # создаем текстовую метку
    label8.pack()  # размещаем метку в окне
    print("Часовой пояс и время:")
    label6 = Label(text=(timezone, now))  # создаем текстовую метку
    label6.pack()  # размещаем метку в окне
    print(timezone, now)

# определить место по координатам

    def get_addr(location: list) -> str:
        try:
            geo_loc = Nominatim(user_agent="GetLoc")
            loc_name = geo_loc.reverse(location)
            return loc_name.address
        except GeocoderUnavailable:
            return 'Неизвестно'

    def main() -> None:
        label9 = Label(text="Адрес центра города: ")  # создаем текстовую метку
        label9.pack()  # размещаем метку в окне
        print("Адрес центра города: ")
        label6 = Label(text=(",".join(reversed(get_addr([latitude, longitude]).split(","))).strip()))  # создаем текстовую метку
        label6.pack()  # размещаем метку в окне
        print(",".join(reversed(get_addr([latitude, longitude]).split(","))).strip())
    if __name__ == "__main__":
        main()


label = ttk.Label() #продолжение
label.pack(anchor=NW, padx=6, pady=6)

label["text"] = entry.get()

btn = ttk.Button(text="Найти!", command=location)
btn.pack(anchor=NW, padx=6, pady=6)

root.mainloop()



