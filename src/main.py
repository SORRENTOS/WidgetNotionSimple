import flet as ft


def main(page: ft.Page):







    page.add(
        ft.SafeArea(
            ft.Text("hola"),
            expand=True,
        )
    )


ft.app(main)
