import qrcode

# Create an instance of QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data('https://github.com/kyalo-45/Techie')
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color='black', back_color='white')  # fill_color and back_color parameters

# Save the image
img.save('Techie_qr.png')

print("QR code generated and saved as Techie_qr.png")
