import flet as ft


def main(page: ft.Page):




    boton1 = ft.Button("\U0001F4E7 Outlook", bgcolor=ft.Colors.BLUE,width=150,height=50,style= ft.ButtonStyle(
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
