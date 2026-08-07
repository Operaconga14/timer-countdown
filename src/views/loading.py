import flet as ft
from src.utils.colors import COLORS
import asyncio
import random
from src.utils.tasks import tasks
from src.views.dashboard import dashboard

async def loading(page: ft.Page):
    page.padding = 0

    current_percent = 0
    task_duration = random.uniform(1, 8)
    duration = random.uniform(0.06, 1)

    # progress update function
    async def load_app(page, progress, progress_text, status_text):
        nonlocal current_percent
        for text, target_percent in tasks:
            status_text.value = text

            for p in range(current_percent, target_percent + 1):
                progress.value = p / 100
                progress_text.value = f"{p}%"
                page.update()
                await asyncio.sleep(duration) 

            current_percent = target_percent
            await asyncio.sleep(task_duration)






    # components
    logo = ft.Image(src="/logo.png", width=200, height=200, fit=ft.BoxFit.CONTAIN)
    title = ft.Text("Operaconga Timer", size=50, weight=ft.FontWeight.W_900)
    sub_text =ft.Text(f"",size=16, color=ft.Colors.WHITE, weight=ft.FontWeight.W_200, italic=True)
    progress_bar = ft.ProgressBar(value=current_percent, color=COLORS["brand_gold"], height=9, width=600, border_radius=30)
    progress_value = ft.Text(f"{progress_bar.value}%", size=16, color=ft.Colors.WHITE)


    layout = ft.SafeArea(
        expand=True,
        content=ft.Container(
            image=ft.DecorationImage(src="/bg1.jpg", fit=ft.BoxFit.COVER),
            content=ft.Column(
                controls=[logo, title, sub_text, progress_bar, progress_value],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            alignment=ft.Alignment.CENTER,
            expand=True
        )
    )


    page.add(layout)

    if current_percent == 100:
        page.clean()
        await dashboard(page)
    else:
        await load_app(page, progress_bar, progress_value, sub_text)
        await asyncio.sleep(3)
        page.clean()
        await dashboard(page)

