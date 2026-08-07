import flet as ft
from src.utils.colors import COLORS
from src.views.overview import overview
from src.views.timers import timers
from src.views.add_timer import add_timer
from src.views.design_timer import design_timer
from src.views.settings import settings
from src.views.output_screen import output_screen
from src.views.service_plan import service_plan

async def dashboard(page: ft.Page):
    page.window.frameless = False
    page.padding = 0

    # Screen Functions
    async def show_overview():
        main_layout.content = await overview()
        page.update()

    async def show_timers():
        main_layout.content = await timers()
        page.update()

    async def show_add_timer():
        main_layout.content = await add_timer()
        page.update()

    async def show_design_timer():
        main_layout.content = await design_timer()
        page.update()

    async def show_settings():
        main_layout.content = await settings()
        page.update()

    async def show_output_screen():
        main_layout.content = await output_screen()
        page.update()

    async def show_service_plan():
        main_layout.content = await service_plan()
        page.update()


    # sidebar components
    sidebar_header_logo = ft.Image(src="/logo.png", width=50, height=50)
    sidebar_header_title = ft.Text("OPERACONGA", size=20, weight=ft.FontWeight.W_900)
    dashboard_btn = ft.TextButton(content=ft.Row(controls=[ft.Icon(ft.Icons.HOUSE_OUTLINED, weight=10, size=22, color=COLORS["text_primary"]), ft.Text("Dashboard", color=COLORS["text_primary"], size=14, weight=ft.FontWeight.W_300)]), height=50, align=ft.Alignment.CENTER, on_click=show_overview)
    timer_btn = ft.TextButton(content=ft.Row(controls=[ft.Icon(ft.Icons.ALARM_ON_OUTLINED, weight=10, size=22, color=COLORS["text_primary"]), ft.Text("Timer", color=COLORS["text_primary"], size=14, weight=ft.FontWeight.W_300)]), height=50, align=ft.Alignment.CENTER, on_click=show_timers)
    add_timer_btn  = ft.TextButton(content=ft.Row(controls=[ft.Icon(ft.Icons.ALARM_ADD_OUTLINED, weight=10, size=22, color=COLORS["text_primary"]), ft.Text("Add Timer", color=COLORS["text_primary"], size=14, weight=ft.FontWeight.W_300)]), height=50, align=ft.Alignment.CENTER, on_click=show_add_timer)
    design_timer_btn  = ft.TextButton(content=ft.Row(controls=[ft.Icon(ft.Icons.AUTO_FIX_HIGH_OUTLINED, weight=10, size=22, color=COLORS["text_primary"]), ft.Text("Design Timer", color=COLORS["text_primary"], size=14, weight=ft.FontWeight.W_300)]), height=50, align=ft.Alignment.CENTER, on_click=show_design_timer)
    settings_btn =  ft.TextButton(content=ft.Row(controls=[ft.Icon(ft.Icons.SETTINGS_OUTLINED, weight=10, size=22, color=COLORS["text_primary"]), ft.Text("Settings", color=COLORS["text_primary"], size=14, weight=ft.FontWeight.W_300)]), height=50, align=ft.Alignment.CENTER, on_click=show_settings)
    output_screen_btn =  ft.TextButton(content=ft.Row(controls=[ft.Icon(ft.Icons.MONITOR_OUTLINED, weight=10, size=22, color=COLORS["text_primary"]), ft.Text("Output Screen", color=COLORS["text_primary"], size=14, weight=ft.FontWeight.W_300)]), height=50, align=ft.Alignment.CENTER, on_click=show_output_screen)
    service_plan_btn =  ft.TextButton(content=ft.Row(controls=[ft.Icon(ft.Icons.LIBRARY_BOOKS_OUTLINED, weight=10, size=22, color=COLORS["text_primary"]), ft.Text("Service Plan", color=COLORS["text_primary"], size=14, weight=ft.FontWeight.W_300)]), height=50, align=ft.Alignment.CENTER, on_click=show_service_plan)

    # sidebar container and layout
    sidebar_header_container = ft.Row(
        controls=[sidebar_header_logo, sidebar_header_title],
        alignment=ft.MainAxisAlignment.CENTER,
        height=120
    )
    sidebar_buttons_container = ft.Container(
        content=ft.Column(
        controls=[
            dashboard_btn,
            timer_btn,
            add_timer_btn,
            design_timer_btn,
            settings_btn,
            output_screen_btn,
            service_plan_btn
            
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10
    ),
    alignment=ft.Alignment.CENTER,
    padding=ft.Padding.only(left=15, right=15)
    )
    sidebar_layout = ft.Container(
        width=250,
        bgcolor=COLORS["sidebar_bg"],
        border=ft.Border.only(right=ft.BorderSide(2, COLORS["brand_navy"])),
        content=ft.Column(
        controls=[sidebar_header_container, sidebar_buttons_container]
        )
    )

    # End of Sidebar
    
    main_layout = ft.Container(
        bgcolor=COLORS["panel_bg"],
        content=await overview(),
        expand=True
    )

    
    # main layout that holds both sidebar and main
    dashboard_layout = ft.SafeArea(
        expand=True,
        content=ft.Container(
            content=ft.Row(
                controls=[sidebar_layout, main_layout],
                spacing=0
            ),
            padding=0,
        )
        
    )

    page.add(dashboard_layout)