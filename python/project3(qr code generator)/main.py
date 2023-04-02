# install all libraries
# create a function taht colects a text and convert it to a qrcode
# save the qrcode as image
#run the function

import qrcode


text = input("inter the link here:")


def generate_qrcode(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg.png")

generate_qrcode(text)

