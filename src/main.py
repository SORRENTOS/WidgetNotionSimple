import flet as ft
import time
import asyncio
def main(page: ft.Page):


    page.bgcolor = ft.Colors.BLACK
    
    boton1 = ft.ElevatedButton("Outlook", bgcolor=ft.Colors.BLUE,width=150,height=50,icon= ft.Icons.EMAIL_ROUNDED,style= ft.ButtonStyle(
        shape= ft.RoundedRectangleBorder(radius=10)),url="https://outlook.office.com/mail/")
    
    boton3 = ft.ElevatedButton("\U0001F4D5 BANNER", bgcolor=ft.Colors.RED,width=150,height=50,style= ft.ButtonStyle(
        shape= ft.RoundedRectangleBorder(radius=10)),url="https://uacloud.uautonoma.cl/dashboard")
    Hora_texto = ft.Text(size=30,weight=ft.FontWeight.BOLD,expand=True,text_align=ft.TextAlign.CENTER) 
    Minuto_texto = ft.Text(size=30,weight=ft.FontWeight.BOLD,expand=True,text_align=ft.TextAlign.CENTER) 
    Segundos_texto = ft.Text(size=30,weight=ft.FontWeight.BOLD,expand=True,text_align=ft.TextAlign.CENTER) 

    container_hora = ft.Container(content=Hora_texto,width=45,height=50,bgcolor=ft.Colors.GREY_900,border_radius=10)
    container_Minutos = ft.Container(content=Minuto_texto,width=45,height=50,bgcolor=ft.Colors.GREY_900,border_radius=10)
    container_Segundos = ft.Container(content=Segundos_texto,width=45,height=50,bgcolor=ft.Colors.GREY_900,border_radius=10)
    fila_tiempo = ft.Row([container_hora,ft.Text(":",weight=ft.FontWeight.BOLD,size=30,expand=True,text_align=ft.TextAlign.CENTER),container_Minutos,ft.Text(":",weight=ft.FontWeight.BOLD,size=30),container_Segundos],spacing=1)
    container_reloj = ft.Container(content=fila_tiempo,bgcolor=ft.Colors.GREY_800,padding=5,border_radius=10)




    async def actualizar_reloj():
        while True:
            Hora_texto.value = f'{time.strftime("%H"):02}'
            Minuto_texto.value = f'{time.strftime("%M"):02}'
            Segundos_texto.value = f'{time.strftime("%S"):02}'


            page.update()
            await asyncio.sleep(1)

    
    fila_botones = ft.Row([boton1,boton3,container_reloj],spacing=50)
    page.add(
        ft.SafeArea(
            fila_botones,
            expand=True,
         )
    )
    
    page.run_task(actualizar_reloj)
ft.app(main)
