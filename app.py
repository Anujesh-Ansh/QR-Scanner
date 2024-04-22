import qrcode
from PIL import Image

message = input("Enter the message: ")
code = qrcode.make(message)
code.save("qrcode.png")

QR = Image.open("qrcode.png")
QR.show()