from time import sleep

import flet as ft

def main(page : ft.Page):
    # CREO UN OGGETTO/CONTROLLO DI TIPO Text
    myText = ft.Text(value = "Hello world!",
                     size = 50,
                     color = "red")
    # LO AGGIUNGO ALLA PAGINA
    page.controls.append( myText )
    # DEVO RICORDARMI DI AGGIORNARE LA PAGINA
    page.update()

    myText.color = "blue"
    #sleep(5)
    myText.update()

    # DEFINISCO LA FUNZIONE EVENT HANDLER DEL CLICK SUL PULSANTE btnPress
    def btnPressHandler(e):
        print("Button pressed")
        myText.color = "green"
        myText.update()

                                                    # INDICO LA FUNZIONE EVENT HANDLER
    btnPress = ft.ElevatedButton(text="Premi qui!", on_click=btnPressHandler )
    page.controls.append(btnPress)
    page.update()


ft.app(target=main, view = ft.AppView.FLET_APP)