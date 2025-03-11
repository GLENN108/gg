import qrcode

hotel_url = "https://www.google.com/maps/place/Park+Elanza/@13.0564501,80.2402965,17z/data=!3m1!5s0x3a52665d3147170f:0x5347dd7fee28663!4m20!1m10!3m9!1s0x3a526752ce62a343:0x30e769c8eec95a10!2sPark+Elanza!5m2!4m1!1i2!8m2!3d13.0564501!4d80.2428714!16s%2Fg%2F11h249t74y!3m8!1s0x3a526752ce62a343:0x30e769c8eec95a10!5m2!4m1!1i2!8m2!3d13.0564501!4d80.2428714!16s%2Fg%2F11h249t74y?entry=ttu&g_ep=EgoyMDI0MTIwMy4wIKXMDSoASAFQAw%3D%3D"

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(hotel_url)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")

img.save("Park_Elanza_QR_Code.png")

print("QR Code saved as 'Park_Elanza_QR_Code.png")
