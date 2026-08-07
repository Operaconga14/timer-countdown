import flet as ft
from src.utils.colors import COLORS

async def design_timer():
    text = ft.Text("Design Timer", size=30)


    return ft.Column(
        controls=[text]
    )