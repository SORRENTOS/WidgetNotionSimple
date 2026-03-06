import flet as ft
import time
import asyncio
def main(page: ft.Page):


    page.bgcolor = ft.Colors.BLACK
    
    boton1 = ft.ElevatedButton("Outlook", bgcolor=ft.Colors.BLUE,width=150,height=50,icon= ft.Icons.EMAIL_ROUNDED,style= ft.ButtonStyle(
        shape= ft.RoundedRectangleBorder(radius=10)),url="https://outlook.office.com/mail/")
    
    boton3 = ft.ElevatedButton("\U0001F4D5 BANNER", bgcolor=ft.Colors.RED,width=150,height=50,style= ft.ButtonStyle(
        shape= ft.RoundedRectangleBorder(radius=10)),url="https://uacloud.uautonoma.cl/dashboard")
    Hora_texto = ft.Text(size=30,weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER) 
    Minuto_texto = ft.Text(size=30,weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER) 
    Segundos_texto = ft.Text(size=30,weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER) 

    container_hora = ft.Container(content=Hora_texto,width=45,height=50,bgcolor=ft.Colors.GREY_900,border_radius=10)
    container_Minutos = ft.Container(content=Minuto_texto,width=45,height=50,bgcolor=ft.Colors.GREY_900,border_radius=10)
    container_Segundos = ft.Container(content=Segundos_texto,width=45,height=50,bgcolor=ft.Colors.GREY_900,border_radius=10)
    fila_tiempo = ft.Row([container_hora,ft.Text(":",weight=ft.FontWeight.BOLD,size=30,text_align=ft.TextAlign.CENTER),container_Minutos,ft.Text(":",weight=ft.FontWeight.BOLD,size=30),container_Segundos],spacing=1)
    container_reloj = ft.Container(content=fila_tiempo,bgcolor=ft.Colors.GREY_800,padding=5,border_radius=10,width=170)

    texto_clase_actual = ft.Text(value="CLASE",size=15,weight=ft.FontWeight.BOLD,expand=True,text_align=ft.TextAlign.CENTER)
    container_Clase_actual = ft.Container(content=texto_clase_actual,height=60,width=120,bgcolor=ft.Colors.GREY_900,border_radius=10,alignment=ft.Alignment.CENTER)
    columan_clase_actual = ft.Column(
    [ft.Text("clase actual/siguiente"), container_Clase_actual],
    alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER
)


    async def actualizar_reloj():
        while True:
            Hora_texto.value = f'{time.strftime("%H"):02}'
            Minuto_texto.value = f'{time.strftime("%M"):02}'
            Segundos_texto.value = f'{time.strftime("%S"):02}'
            HORA= time.strftime("%H")
            MINUTO= time.strftime("%M")

            nombre_dia = time.strftime("%A")
            #print(tiempo_completo)
            if nombre_dia == "Monday":
                #SEGURIDAD DE REDES 9:30- 10.50
                if  int(HORA) < 10 or (int(MINUTO) < 50 and int(HORA) == 10):
                    texto_clase_actual.value = "REDES \n A 2inf \n 9:30-10:50"
         
                #Humanista 3.30-6.20
                elif  int(HORA) < 18 or (int(MINUTO) < 20 and int(HORA) == 18):
                    texto_clase_actual.value = "HUMANISTA \n A 106 \n 3:30-6:20"
                else: 
                    texto_clase_actual.value = "SALIDA"
                         
            elif nombre_dia == "Tuesday":
                #ALGEBRA
                if  int(HORA) < 13 or (int(MINUTO) < 10 and int(HORA) == 13):
                    texto_clase_actual.value = "ALGEBRA \n A 221 \n 11:00-1:10"
                #ANALISIS
                elif  int(HORA) < 15 or (int(MINUTO) < 20 and int(HORA) == 15):
                    texto_clase_actual.value = "ANALISIS \n A 335 \n 2:00-3:20"
                else: 
                    texto_clase_actual.value = "SALIDA"
            elif nombre_dia == "Wednesday":
                #SEGURIDAD DE REDES 9:30- 10.50
                if  int(HORA) < 10 or (int(MINUTO) < 50 and int(HORA) == 10):
                    texto_clase_actual.value = "REDES \n C 001 \n 9:30-10:50"
                #CONTABILIDAD
                elif  int(HORA) < 16 or (int(MINUTO) < 50 and int(HORA) == 16):
                    texto_clase_actual.value = "CONTABILIDAD \n A 441 \n 3:30-4:50"
                else: 
                    texto_clase_actual.value = "SALIDA"
                         
            elif nombre_dia == "Thursday":
                #INGLES 
                if  int(HORA) < 12 or (int(MINUTO) < 20 and int(HORA) == 12):
                    texto_clase_actual.value = "INGLES \n A 224 \n 11:00-12:00"
                elif  int(HORA) < 14 or (int(MINUTO) < 20 and int(HORA) == 15):
                    texto_clase_actual.value = "ALGEBRA A \n A 101 \n 2:00-3:20"
                else: 
                    texto_clase_actual.value = "SALIDA"
            elif nombre_dia == "Friday":
                #INGLES 
                if  int(HORA) < 10 or (int(MINUTO) < 50 and int(HORA) == 10):
                    texto_clase_actual.value = "INGLES \n A 334 \n 9:30-10:50"
                #contabilidad
                elif  int(HORA) < 15 or (int(MINUTO) < 20 and int(HORA) == 15):
                    texto_clase_actual.value = "CONTABILIDAD \n A 102 \n 2:00-3:20"
                #analisis
                elif  int(HORA) < 16 or (int(MINUTO) < 50 and int(HORA) == 50):
                    texto_clase_actual.value = "ANALISIS \n C LC ING \n 3:30-4:50"
                else: 
                    texto_clase_actual.value = "SALIDA"
            else:
                texto_clase_actual.value = "ES FINDEE :D"
            page.update()
            await asyncio.sleep(1)

    
    fila_botones = ft.Row([boton1,boton3,container_reloj,columan_clase_actual],vertical_alignment=ft.MainAxisAlignment.CENTER,spacing=50,wrap=True)
    page.add(
        ft.SafeArea(
            fila_botones,
            expand=True,
         )
    )
    
    page.run_task(actualizar_reloj)
ft.app(main)
