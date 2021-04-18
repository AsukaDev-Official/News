from tkinter import *
import requests, json

window = Tk()
window.title("Open News By Tegar Dev")
window.geometry('700x200')

lbl = Label(window, text="Klik Button Untuk Mencari Berita  ", font=("Roboto", 16))
lbl.grid(column=0, row=0)

def clicked():
  link='https://opennewsapi.herokuapp.com/api/news/'
  try:
    req=requests.get(link)
    jeson=json.loads(req.text)
  except requests.ConnectionError:
    result = Label(window, text='koneksi tidak ada', font=("Roboto", 14)).grid(pady=1)
  for data in jeson['results']:
    under = 60*'='
    sumber = data['source']
    tag = data['tag']
    tanggal = data['created_at']
    judul = data['title']
    link = data['link']
    gambar  = data['image']
    result = Label(window, text=f'Sumber : {sumber}\ntag : {tag}\ntanggal : {tanggal}\njudul : {judul}\nlink : {link}\ngambar : {gambar}', font=("Roboto", 12)).grid(pady=1)

btn = Button(window, text="Cari Berita", command=clicked)
btn.grid(column=2, row=0)

window.mainloop()
