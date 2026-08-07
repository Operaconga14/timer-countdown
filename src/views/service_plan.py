import flet as ft
from src.utils.colors import COLORS

async def service_plan():
    text = ft.Text("Service Plan", size=30)


    return ft.Column(
        controls=[text]
    )