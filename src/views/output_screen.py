import flet as ft
from src.utils.colors import COLORS

async def output_screen():
    text = ft.Text("Output Screen", size=30)


    return ft.Column(
        controls=[text]
    )