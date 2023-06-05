import win32clipboard
from io import BytesIO
from PIL import Image

def read_image_from_clipboard():
    win32clipboard.OpenClipboard()
    clipboard_data = win32clipboard.GetClipboardData(win32clipboard.CF_DIB)
    win32clipboard.CloseClipboard()

    if clipboard_data is None:
        return None

    image_data = BytesIO(clipboard_data)
    image = Image.open(image_data)
    return image

def save_image_as_png(image, filename):
    image.save(filename, "PNG")
    print("Image saved as", filename)

clipboard_image = read_image_from_clipboard()
if clipboard_image is not None:
    # Convert the image to PNG and save it
    save_image_as_png(clipboard_image, "clipboard_image.png")
else:
    print("No image found in the clipboard.")