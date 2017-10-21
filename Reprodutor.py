from pygame  import mixer # Carregando a biblioteca do pygame_Evaldo
from tkinter.filedialog import askopenfilename
from tkinter import *


musicas = []
TAM     = len(musicas)

class Reprodutor :
    def __init__ (self):
       pass

    def escolher ():
        selecionar = askopenfilename(initialdir="C:/Users/Desktop",
                           filetypes =(("Arquivo de audio", "*.mp3"),("All Files","*.*")),
                           title = "Selecione as musicas",

                           )
        musicas.append(selecionar)


        for i in musicas:
            print(i, end=" ")
            print()
        print()


        return musicas

    def reproduzir ():
        mixer.init()

        for item in musicas:
            musica_atual = mixer.music.load(item)
            musica_atual = mixer.music.play()

    def parar ():
        musica_atual = mixer.music.stop()

    def pausar ():
        musica_atual = mixer.music.pause()

    def continuar ():
        musica_atual = mixer.music.unpause() #Continua do local pausado

#Bug da troca de música corrigido
        
    def proxima ():
        for item in range(len(musicas)):

            item += 1
            musica_atual = mixer.music.load(musicas[item])
            musica_atual = mixer.music.play()

    def anterior ():
        for item in range(len(musicas)):
            item -= 1
            musica_atual = mixer.music.load(musicas[item])
            musica_atual = mixer.music.play()

