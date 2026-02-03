import qrcode
img = qrcode.make('https://github.com/devae0')
type(img)
img.save("qrtry2.png")
