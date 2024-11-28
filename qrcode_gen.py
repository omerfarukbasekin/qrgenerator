import qrcode_gen

# Define the data you want to encode in the QR code
data = "Hello, World!"

# Create an instance of the QRCode class
qr = qrcode_gen.QRCode(version=1, error_correction=qrcode_gen.constants.ERROR_CORRECT_L, box_size=10, border=4)

# Add the data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
qr_img = qr.make_image(fill_color="black", back_color="white")

# Save the image
qr_img.save("qr_code.png")
