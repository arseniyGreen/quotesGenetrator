# based on https://github.com/NotCookey/Quote2Image
from Quote2Image import Convert, GenerateColors, ImgObject
from datetime import datetime

def genImage(quote_text="Пример цитаты", author_text="Пример ссылки", font_size=32):
    # Generate Fg and Bg Color
    fg, bg = GenerateColors()

    img=Convert(
        quote=quote_text,
        author=author_text,
        fg=fg,
        bg=bg,
        font_size=32,
        font_type="arial.ttf",
        width=1080,
        height=450,
        watermark_text="@oz_mol",
        watermark_font_size=12
        )

    # Save The Image as a Png file
    img_path = "output/"+genImageName()+".png"
    img.save(img_path)
    return img_path

def genImageName():
    now = datetime.now()
    name = now.strftime("%d-%m-%Y_%H-%M-%S")
    return name

def main():
    quote = input("Quote: ")
    author = input("Auth: ")
    font_size = input("f_size: ")
    genImage(quote, author, font_size)
    genImage()