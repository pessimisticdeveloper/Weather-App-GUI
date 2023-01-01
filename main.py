from tkinter import *
from PIL import ImageTk,Image
import requests

url = 'https://api.openweathermap.org/data/2.5/weather'
api_key = '429361fa0d1602a4fe4e7d5a5a23d368'
iconUrl = 'http://openweathermap.org/img/wn/{}@2x.png'

uygulama = Tk()
uygulama.geometry('300x450')
uygulama.title('hava durumu')

def havaDurumu(sehir):
    params = {'q':sehir,'appid':api_key}
    data = requests.get(url,params=params).json()
    if data:
        sehir = data['name'].capitalize()
        ulke = data['sys']['country']
        sicaklik = int(data['main']['temp'] - 273.15)
        icon = data['weather'][0]['icon']
        condition = data['weather'][0]['description']
        return (sehir,ulke,sicaklik,icon,condition)

def main():
    sehir = sehirEntry.get()
    havadurumu = havaDurumu(sehir)
    if havadurumu:
        sehir_bilgileri['text'] = '{},{}'.format(havadurumu[0],havadurumu[1])
        sicaklik['text'] = '{}C'.format(havadurumu[2])
        conditionLabel['text'] = havadurumu[4]
        icon = ImageTk.PhotoImage(Image.open(requests.get(iconUrl.format(havadurumu[3]),stream=True).raw))
        iconLabel.configure(image=icon)
        iconLabel.image = icon

sehirEntry = Entry(uygulama,justify='center')
sehirEntry.pack(fill=BOTH,ipadx=10,padx=18,pady=5)
sehirEntry.focus()

aramaButton = Button(uygulama,text='Arama',font=('Arial',15,'bold'),command=main)
aramaButton.pack(fill=BOTH,ipady=10,ipadx=20)

iconLabel = Label(uygulama)
iconLabel.pack()

sehir_bilgileri = Label(uygulama,font=('Arial',40))
sehir_bilgileri.pack()

sicaklik = Label(uygulama,font=('Arial',50,'bold'))
sicaklik.pack()

conditionLabel = Label(uygulama,font=('Arial',20))
conditionLabel.pack()

uygulama.mainloop()
