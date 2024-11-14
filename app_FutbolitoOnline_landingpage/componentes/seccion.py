import reflex as rx
def seccion()->rx.Component:
  return rx.vstack(
      rx.image(src="/cuadro de torneo.jpg", width="50%", height="auto"),
      rx.heading(
        rx.text(" Diseña tu torneo ideal ",size="9",color="#f2d307"),
        rx.text("¡Las reglas lo pones tú!",size="9",color="#0736f2")),

      rx.container(
        rx.text("-Ahorra tiempo y esfuerzo en la organizacion de torneos .",color="#0b13ef"),
        rx.text("-Crea torneos memorables y exitosos deacuerdo a tu estilo .",color="#0b13ef"),
        rx.text("-Manten a tus participantes informados con notificaciones.",color="#0b13ef"),
        rx.link(rx.button("REGISTRATE",margin_top="4em",color_scheme="cyan"),href="https://forms.gle/Apc6aXEWNma79Nfs7",is_external=True),
        margin_top="1em"
      ),
  
      background="url('../assets/futbol y copa.png')",
      padding_top="8em",
      align="center",
      text_align="center",
      #background="linear-gradient(0deg, rgba(14,12,135,1) 0%, rgba(0,0,0,1) 100%)",
      height="800px",
      color="#030e3a",
    )