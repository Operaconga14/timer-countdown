import flet as ft
from src.utils.colors import COLORS

async def splash(page: ft.Page):
    page.window.frameless = True
    page.padding = 0

    # components
    logo = ft.Image(src="/logo.png", width=200, height=200, fit=ft.BoxFit.CONTAIN)
    title = ft.Text("Operaconga Timer", size=50, weight=ft.FontWeight.W_900)
    sub_text = ft.Text("Every moment. Purposefully counted.", size=20, color=COLORS["brand_gold"])

    # layout
    layout = ft.SafeArea(
        expand=True,
        content=ft.Container(
            image=ft.DecorationImage(src="/bg1.jpg", fit=ft.BoxFit.COVER),
            content=ft.Column(
            controls=[logo, title, sub_text],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            alignment=ft.Alignment.CENTER,
            expand=True
        )
        )
   

    page.add(layout)