import flet as ft
import asyncio
from src.views.dashboard import dashboard
from src.views.spalsh import splash
from src.views.loading import loading


async def main(page: ft.Page):
    page.window.frameless = True
    page.window.maximized = True
    page.title = "Operaconga Timer"

    # await splash(page)
    # page.update()

    # await asyncio.sleep(10)
    # page.clean()

    # await loading(page)
    # page.update()

    await dashboard(page)
    page.update()


if __name__ == "__main__":
    # FIX: Pass 'main' explicitly into the target argument
    ft.run(main, assets_dir="assets")