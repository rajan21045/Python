import qrcode
import os

try:
    data = input("Enter data: ").strip()
    if not data:
        raise ValueError("Data cannot be empty")

    filename = input("Enter filename: ").strip() or "qrcode.png"
    
    # Force extension if missing
    if "." not in filename:
        filename += ".png"

    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")
    image.save(filename)

    print(f"Success! Saved to: {os.path.abspath(filename)}")

except Exception as e:
    print(f"Failed to save: {e}")