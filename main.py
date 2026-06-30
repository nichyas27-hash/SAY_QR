from nicegui import ui, app
from panels import tab_url, tab_img, tab_pdf, tab_video, tab_audio

import os

app.add_static_files('/uploads', 'uploads')
ui.add_head_html("""
    <link rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
    """)

with ui.header().props('flex').classes('w-full').style("""
    background-color: #ffffff; 
    align-content:center; 
    justify-content:space-between;"""):

    ui.image("assets/icons/Logo.png").style("width: 150px")
    with ui.row().style("""
            color: #000;
            font-size: 28px;
            """):
        ui.html("""<a href="https://github.com/nichyas27-hash" target="_blank"><i class="fab fa-github"></i></a>""")
        ui.html("""<a href="https://nichyas27.site" target="_blank"><i class="fas fa-user"></i></a>""")

with ui.row().classes('w-full flex'):
    ui.image("assets/ani/Cute Robot Flying Cartoon.svg").classes('w-2/12 items-center').style("width: 200px; height: 150px")
    ui.html("""
    <h4 class="m-0"> Create & Custumize Dynamic QR Code for Free</h3>
    <h6 class="-mt-10">Easily generate, manage, and track your dynamic QR Codes.</h6>
    """).classes('w-8/12 flex items-center justify-center').style("height:150px")
    ui.image("assets/ani/Welcome Animation.svg").classes('w-2/12 items-center').style("width: 200px; height: 150px")

with ui.column().classes('w-full flex flex-col').style("background-color: #fafbff"):
    with ui.row().classes('w-full mt-10').style("background-color: #ffffff"):
        with ui.tabs().props('inline-label').classes('w-full').style("border-radius: 10px") as tabs:
            url = ui.tab('URL/link', icon='link')
            image = ui.tab('Image', icon='image')
            pdf = ui.tab('PDF', icon='picture_as_pdf')
            video = ui.tab('Video', icon='videocam')
            audio = ui.tab('Audio', icon='audiotrack')
    
    with ui.row().classes('w-full justify-center'):
        with ui.tab_panels(tabs, value=url).classes('w-full'):
            with ui.tab_panel(url).classes('w-full flex flex-col items-center'):
                tab_url()

            with ui.tab_panel(image).classes('w-full flex flex-col items-center'):
                tab_img()

            with ui.tab_panel(pdf).classes('w-full flex flex-col items-center'):
                tab_pdf()

            with ui.tab_panel(video).classes('w-full flex flex-col items-center'):
                tab_video()

            with ui.tab_panel(audio).classes('w-full flex flex-col items-center'):
                tab_audio()

    with ui.row().classes('w-full flex mt-10 justify-center').style("background-color: #ffffff"):
        with ui.column().classes('w-1/6 items-stretch'):
            ui.image("assets/icons/Logo.png").classes('mt-10').style("width: 150px; align-content: center")
        with ui.column().classes('w-1/6 items-stretch'):
            ui.image("assets/ani/Robot Says Hi.svg").classes('mt-2').style("height: 100px; width:100px; align-content: center")
        with ui.column().classes('w-1/6 items-stretch'):
            ui.label("Getting to Know Me").classes('mt-7').style("font-size: 20px")
            ui.html("""<div class="flex gap-3 w-full -mt-5">
            <a href="https://www.instagram.com/yassaya__?igsh=Z2U1Y2pjbHo2MzRr" target="_blank"><i class="fab fa-instagram"></i></a>
            <a href="https://www.facebook.com/Yass4ya" target="_blank"><i class="fab fa-facebook"></i></a>
            <a href="https://github.com/nichyas27-hash" target="_blank"><i class="fab fa-github"></i></a>
            <a href="https://www.linkedin.com/in/jaya-perkasa/" target="_blank"><i class="fab fa-linkedin"></i></a>
            </div>""").style("font-size: 20px")
        with ui.column().classes('w-1/6 items-stretch'):
            ui.image("assets/ani/thank you #566dfb.svg").style("width: 200px; height: 100px")
        with ui.column().classes('w-1/6 items-stretch'):
            ui.label("© 2026 SAY QR. All rights reserved.").classes('mt-20 justify-right').style("font-size: 12px")

ui.run(
    host='0.0.0.0',
    port=int(os.environ.get('PORT', 8080)),
)