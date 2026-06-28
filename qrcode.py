import qrcode
qr=qrcode.make(input("Enter Your Secrets: "))
qr.save("secretmessage.png")