import flet as ft
from src.utils.colors import COLORS

async def settings():
    text = ft.Text("Settings", size=30)


    return ft.Column(
        controls=[text]
    )