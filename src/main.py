import flet as ft


def main(page: ft.Page):




    boton1 = ft.ElevatedButton("Outlook", bgcolor=ft.Colors.BLUE,width=150,height=50,icon= ft.Icons.EMAIL_ROUNDED,style= ft.ButtonStyle(
        shape= ft.RoundedRectangleBorder(radius=10)),url="https://outlook.office.com/mail/")
    
    boton3 = ft.ElevatedButton("\U0001F4D5 BANNER", bgcolor=ft.Colors.RED,width=150,height=50,style= ft.ButtonStyle(
        shape= ft.RoundedRectangleBorder(radius=10)),url="https://uacloud.uautonoma.cl/dashboard")



    
    fila_botones = ft.Row([boton1,boton3],spacing=100)
    page.add(
        ft.SafeArea(
            fila_botones,
            expand=True,
         )
    )


ft.app(main)
