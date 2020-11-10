import PIL
from PIL import ImageFont, Image, ImageDraw
import csv, os, shutil

X_SIZE = 1920
Y_SIZE_PERSONAL_INFO = 320
Y_SIZE_COURSE_NAME = 620
Y_SIZE_REALIZATION_DATE = 940


def get_size_line(text_font, data):
    lines = data.splitlines()

    if (len(lines) > 1):
        max_size_line = max(lines,key=lambda line: len(line))
        return text_font.getsize(max_size_line)[0]
    else:
        return text_font.getsize(data)[0]

def get_x_coordinate(font,data):
    return (X_SIZE - get_size_line(font,data)) / 2

def course_cert_generate(full_name, identification_number):
    personal_data_font = ImageFont.truetype("fonts/Lato-Black.ttf",45)
    info_data_font = ImageFont.truetype("fonts/Lato-Bold.ttf",45)
    footer_data_font = ImageFont.truetype("fonts/Lato-Bold.ttf",40)

    imageFile = "template.jpg"
    im1=Image.open(imageFile)
    draw = ImageDraw.Draw(im1)

    personal_data = "{}\n{}".format(full_name,identification_number)
    draw.text(
        (
            get_x_coordinate(personal_data_font,personal_data),
            Y_SIZE_PERSONAL_INFO
        ),
        personal_data,
        (0,0,0),
        align='center',
        font=personal_data_font)

    course_name = "DISEÑO DE REVISTA DIGITAL"
    draw.text(
        (
            get_x_coordinate(info_data_font, course_name),
            Y_SIZE_COURSE_NAME
        ),
        course_name,
        (0,0,0),
        align="center",
        font=info_data_font)

    date_of_realization = "Realizado los días 11, 12 y 13 de Noviembre de 2020\nCON UN TOTAL DE 7 HORAS CATEDRA"
    draw.text(
        (
            get_x_coordinate(footer_data_font,date_of_realization),
            Y_SIZE_REALIZATION_DATE
        ),
        date_of_realization,
        (0,0,0),
        align="center",
        font=footer_data_font
    )

    im1.save( "records/{}.pdf".format(full_name))

def clean_data():
    folder_data = "records"
    shutil.rmtree(folder_data)
    os.mkdir(folder_data)


if __name__=="__main__":
    clean_data()
    with open("data.csv", newline="") as File:
        reader = csv.reader(File)
        for row in reader:
            course_cert_generate(row[0],row[1])
