import segno
from tkinter import *


def generateqr():
    qrcode = segno.make_qr(info.get())
    qrcode.save(
        f"{papka.get()}/{name.get()}.png",
        scale=int(size.get()),
        border=int(size2.get()),
    )

    sozdano = Label(window, text="QR-код успешно создан", fg="green")
    sozdano.grid(column=1, row=11)


window = Tk()
window.title("QR - код генератор")
window.geometry("275x275")


infotxt = Label(window, text="Введите данные, для генерации QR - кода")
infotxt.grid(column=1, row=0)
info = Entry(window, width=25)
info.grid(column=1, row=1)

nametxt = Label(window, text="Введите название QR - кода")
nametxt.grid(column=1, row=2)
name = Entry(window, width=25)
name.grid(column=1, row=3)

sizetxt = Label(window, text="Выберите размер QR - кода")
sizetxt.grid(column=1, row=4)
size = Spinbox(window, from_=1, to=100, width=5)
size.grid(column=1, row=5)

size2txt = Label(window, text="Выберите размер пустой области QR - кода")
size2txt.grid(column=1, row=6)
size2 = Spinbox(window, from_=1, to=100, width=5)
size2.grid(column=1, row=7)

papkatxt = Label(window, text="Выберите путь в папку для сохранения QR - кода")
papkatxt.grid(column=1, row=8)
papka = Entry(window, width=25)
papka.grid(column=1, row=9)

makeqr = Button(window, text="Создать QR - код", command=generateqr)
makeqr.grid(column=1, row=10)


window.mainloop()
