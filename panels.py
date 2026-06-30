from nicegui import ui
from functions import save_file, create_QR, download, remove

def tab_url():
    input = ui.input(label="Type your URL here", placeholder="https://")
    content= ui.image("assets/ani/Robot-Bot 3D.svg").style("width:250px; height:250px")
    ui.button(
        'Create QR Code',
        on_click=lambda: create_QR(url=input.value, content=content)
    )
    content.update()
    with ui.row().classes('w-full justify-center items-center'):
        ui.button("Download", on_click=lambda: download())
        ui.button("Delete", on_click=lambda: remove(content))

def tab_img():
    ui.upload(label="Upload your file here", on_upload=save_file).props('accept=".png,.jpg,.jpeg,.gif,.webp"')
    content = ui.image("assets/ani/Robot-Bot 3D.svg").style("width:250px; height:250px")
    ui.button(
        'Create QR Code',
        on_click=lambda: create_QR(url=None, content=content)
    )
    content.update()
    with ui.row().classes('w-full justify-center items-center'):
        ui.button("Download", on_click=lambda: download())
        ui.button("Delete", on_click=lambda: remove(content))

def tab_pdf():
    ui.upload(label="Upload your file here", on_upload=save_file).props('accept=".pdf"')
    content = ui.image("assets/ani/Robot-Bot 3D.svg").style("width:250px; height:250px")
    ui.button(
        'Create QR Code',
        on_click=lambda: create_QR(url=None, content=content)
    )
    content.update()
    with ui.row().classes('w-full justify-center items-center'):
        ui.button("Download", on_click=lambda: download())
        ui.button("Delete", on_click=lambda: remove(content))

def tab_video():
    ui.upload(label="Upload your file here", on_upload=save_file).props('accept="".mp4,.mov,.avi,.mkv,.webm"')
    content = ui.image("assets/ani/Robot-Bot 3D.svg").style("width:250px; height:250px")
    ui.button(
        'Create QR Code',
        on_click=lambda: create_QR(url=None, content=content)
    )
    content.update()
    with ui.row().classes('w-full justify-center items-center'):
        ui.button("Download", on_click=lambda: download())
        ui.button("Delete", on_click=lambda: remove(content))

def tab_audio():
    ui.upload(label="Upload your file here", on_upload=save_file).props('accept=".mp3,.wav,.ogg,.m4a,.flac"')
    content = ui.image("assets/ani/Robot-Bot 3D.svg").style("width:250px; height:250px")
    ui.button(
        'Create QR Code',
        on_click=lambda: create_QR(url=None, content=content)
    )
    content.update()
    with ui.row().classes('w-full justify-center items-center'):
        ui.button("Download", on_click=lambda: download())
        ui.button("Delete", on_click=lambda: remove(content))    