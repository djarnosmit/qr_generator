import qrcode
import argparse

def generate_qr(data, filename="qrcode.png", version=None, box_size=10, border=4):
    qr = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    print(f"📏 QR version used: {qr.version}")

    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    img.save(filename, format="PNG", optimize=True)
    print(f"✅ QR-code opgeslagen als {filename}")


parser = argparse.ArgumentParser(description="Generate a QR code (WiFi, URL, text, etc).")
parser.add_argument("--data", required=True, help="The data to be included in the QR code (e.g., URL or WiFi config).")
parser.add_argument("--filename", default="qrcode.png", help="Output filename (default: qrcode.png)")
parser.add_argument("--version", type=int, default=None, help="QR code version (1-40). Default: auto")
parser.add_argument("--box_size", type=int, default=10, help="Size of each QR block in pixels (default: 10)")
parser.add_argument("--border", type=int, default=4, help="Border size in blocks (default: 4)")

args = parser.parse_args()

generate_qr(args.data, args.filename, args.version, args.box_size, args.border)
