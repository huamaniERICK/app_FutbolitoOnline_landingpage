import reflex as rx
from .componentes.encabezado import encabezado
from .componentes.seccion import seccion

def index()->rx.Component:
  
  return rx.box(
    encabezado(),
    seccion(),
    background="#07f279",
  )

  


  
    
  

app=rx.App()
app.add_page(index)