import flet as ft
from datetime import datetime
from src.utils.colors import COLORS
from src.utils.time import get_current_date, get_current_time, get_greetings

async def overview():

    # layer 1 components
    # date fetcher
    greeting_text = get_greetings()
    current_date = get_current_date()
    current_time = get_current_time()

    # Greetings
    name_text = "Poter's Ville"
    greetings = ft.Text(f"{greeting_text}, {name_text}", size=30, weight=ft.FontWeight.W_600)
    sub_text = ft.Text("Manage your service timers", size=14, color=ft.Colors.WHITE_54, weight=ft.FontWeight.W_300)

    # Date and time
    cal_icon = ft.Icon(icon=ft.Icons.CALENDAR_MONTH_OUTLINED, color=ft.Colors.WHITE_60, size=30)
    date_text = ft.Text(f"{current_date}", color=ft.Colors.WHITE_70, size=15)
    time_text = ft.Text(f"{current_time}", color=ft.Colors.WHITE, size=18, weight=ft.FontWeight.W_700)

    # layer 1 contaners and layout
    greetings_container = ft.Column(
        controls=[greetings, sub_text],
        spacing=0
    )

    date_fetcher_column = ft.Column(
            controls=[date_text, time_text],
            spacing=0
        )
    
    date_fetcher_row = ft.Row(
        controls=[cal_icon, date_fetcher_column],\
        wrap=True
    )

    layer1_container = ft.Row(
        controls=[greetings_container, date_fetcher_row],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    # Layer 2 components 

    # row 1 components and layouts
    timers_icon  = ft.Icon(icon=ft.Icons.CALENDAR_VIEW_DAY_OUTLINED, color=ft.Colors.LIGHT_BLUE_ACCENT_700)
    timers_count = ft.Text("3", size=30, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)
    timers_text = ft.Text("Timers Today", size=16, color=ft.Colors.WHITE_60)
    timers_column = ft.Column(
            controls=[timers_count, timers_text],
            spacing=0
        )
    timers_row = ft.Row(
            controls=[timers_icon, timers_column],
            wrap=True
        )
    row_1_container = ft.Container(
            content=timers_row,
            bgcolor=COLORS["card_bg"],
            width=200,
            height=100,
            padding=ft.Padding.only(left=30, right=30, top=15, bottom=25),
            border_radius=15,
            border=ft.Border.only(right=ft.BorderSide(2, COLORS["brand_navy"]), left=ft.BorderSide(2, COLORS["brand_navy"]), top=ft.BorderSide(2, COLORS["brand_navy"]), bottom=ft.BorderSide(2, COLORS["brand_navy"]))
        )

    # row 2 components and layouts
    active_icon = ft.Icon(icon=ft.Icons.CALENDAR_VIEW_DAY_OUTLINED, color=ft.Colors.LIGHT_BLUE_ACCENT_700)
    active_count = ft.Text("3", size=30, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)
    active_text = ft.Text("Timers Today", size=16, color=ft.Colors.WHITE_60)
    active_column = ft.Column(
            controls=[active_count, active_text],
            spacing=0
        )
    active_row = ft.Row(
            controls=[active_icon, active_column]
        )
    
    row_2_container = ft.Container(
            content=active_row,
            bgcolor=COLORS["card_bg"],
            width=200,
            height=100,
            padding=ft.Padding.only(left=30, right=30, top=15, bottom=25),
            border_radius=15,
            border=ft.Border.only(right=ft.BorderSide(2, COLORS["brand_navy"]), left=ft.BorderSide(2, COLORS["brand_navy"]), top=ft.BorderSide(2, COLORS["brand_navy"]), bottom=ft.BorderSide(2, COLORS["brand_navy"]))
        )

    # row 3 components and layouts
    total_icon = ft.Icon(icon=ft.Icons.CALENDAR_VIEW_DAY_OUTLINED, color=ft.Colors.LIGHT_BLUE_ACCENT_700)
    total_time = ft.Text("3", size=30, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)
    total_text = ft.Text("Timers Today", size=16, color=ft.Colors.WHITE_60)
    tota_dur_column = ft.Column(
                controls=[total_time, total_text],
                spacing=0
            )
    tota_dur_row = ft.Row(
                controls=[total_icon, tota_dur_column]
            )
    row_3_container = ft.Container(
                content=tota_dur_row,
                bgcolor=COLORS["card_bg"],
                width=200,
                height=100,
                padding=ft.Padding.only(left=30, right=30, top=15, bottom=25),
                border_radius=15,
                border=ft.Border.only(right=ft.BorderSide(2, COLORS["brand_navy"]), left=ft.BorderSide(2, COLORS["brand_navy"]), top=ft.BorderSide(2, COLORS["brand_navy"]), bottom=ft.BorderSide(2, COLORS["brand_navy"]))
            )

    # row 4 components and layouts
    # service_end_icon
    # service_end_time
    # service_end_text

    # row 5 components and layouts
    # empty

    # layer 2 containers and layout

    

   


    layer_2_layout = ft.Row(
        controls=[row_1_container, row_2_container, row_3_container],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        wrap=True
    )

    return ft.SafeArea(
        content=ft.Container(
        content=ft.Column(
            controls=[layer1_container, layer_2_layout],
            expand=True,
            spacing=40
        ),
        padding=ft.Padding.only(left=30, right=30, top=30, bottom=25)
    )
    )