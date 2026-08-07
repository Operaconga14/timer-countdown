import flet as ft
from src.utils.colors import COLORS

async def add_timer():
    text = ft.Text("Add Timer", size=30)


    return ft.Column(
        controls=[text]
    )