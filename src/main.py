import flet as ft


def main(page: ft.Page):




    boton1 = ft.ElevatedButton("Outlook", bgcolor=ft.Colors.BLUE,width=150,height=50,icon= ft.Icons.MAIL_LOCK_ROUNDED,style= ft.ButtonStyle(
        shape= ft.RoundedRectangleBorder(radius=10)



    ))
    fila_botones = ft.Row([boton1])
    page.add(
        ft.SafeArea(
            fila_botones,
            expand=True,
        )
    )


ft.app(main)
