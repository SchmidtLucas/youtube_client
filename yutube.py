from distutils import extension
from pytube import*
from tkinter import*

def botonBuscar():
    def ok():
        s = Search(search_bar.get())
        len(s.results)
    boton_1.pack_forget()
    search_bar = Entry()
    search_bar.pack()
    boton_pack = Button(text="ok", command=ok)
    boton_pack.pack()
    


w = Tk()
boton_1 = Button(text="buscar", command=botonBuscar)
boton_1.pack()

mainloop()

"""
def progress_function(self, stream, bytes_remaining):

    size = stream
    p = 0
    while p <= 100:
        progress = p
        print (str(p)+'%')
        p = percent(bytes_remaining, size)

def percent(self, tem, total):
        perc = (float(tem) / float(total)) * float(100)
        return perc

yt = YouTube("https://youtu.be/BTsB21Xps0Y", on_progress_callback=progress_function, on_complete_callback=print("ultrameganashe"))

yt.streams.filter(progressive=True)


for i in yt.streams:
    print(i)

archivo = yt.streams.get_by_itag(input("mete un numero\n"))
archivo.download()

"""