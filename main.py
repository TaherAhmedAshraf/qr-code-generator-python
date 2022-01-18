import image
import qrcode

data = input("Enter data to be encoded: ")

qr = qrcode.QRCode(
    version=1,
    # error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
# save image
image_title = data.replace(" ", "_")
img.save(f"{image_title}.png")