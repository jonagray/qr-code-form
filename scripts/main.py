import qrcode
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
# URL of the fillable form
form_url = os.getenv('FORM_URL')

print(form_url)

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(form_url)
qr.make(fit=True)

# Create an Image object from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("form_qr_code.png")
