from nicegui import ui
from io import BytesIO
from pathlib import Path

import base64
import qrcode
import os

BASE_URL = os.environ.get(
    'BASE_URL',
    'http://127.0.0.1:8080'
)

UPLOAD_DIR = Path('uploads')
UPLOAD_DIR.mkdir(exist_ok=True)

file = None
async def save_file(e):
    global file

    if e.file.content_type.startswith('image/'):
        folder = Path('uploads/image')
    elif e.file.content_type == 'application/pdf':
        folder = Path('uploads/pdf')
    elif e.file.content_type.startswith('audio/'):
        folder = Path('uploads/audio')
    elif e.file.content_type.startswith('video/'):
        folder = Path('uploads/video')
    else:
        folder = Path('uploads/other')

    folder.mkdir(parents=True, exist_ok=True)

    file = folder / e.file.name
    await e.file.save(file)

    ui.notify(f"Upload Success :3")

QR_buffer = None
def create_QR(url, content):
    global file
    global QR_buffer
    if url is not None:
        img = qrcode.make(url)
        QR_buffer = BytesIO()
        img.save(QR_buffer, format='PNG')
        QR_buffer.seek(0)

        b64 = base64.b64encode(QR_buffer.getvalue()).decode()

        content.set_source(f'data:image/png;base64,{b64}')

    else:
        url = f'{BASE_URL}/{file}'

        img = qrcode.make(url)
        QR_buffer = BytesIO()
        img.save(QR_buffer, format='PNG')
        QR_buffer.seek(0)

        b64 = base64.b64encode(QR_buffer.getvalue()).decode()

        content.set_source(f'data:image/png;base64,{b64}')

def download():
    global QR_buffer

    if QR_buffer is not None:
        QR_Code = QR_buffer.seek(0)

        ui.download(QR_Code, filename="QR_Code.png")

def remove(content):
    global file, QR_buffer
    del file, QR_buffer



    content.set_source(f"assets/ani/Robot-Bot 3D.svg")
