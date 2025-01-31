import qrcode
import argparse


def generate_qr(data, filename="qrcode.png", version=10, box_size=10, border=2):
    qr = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"✅ QR-code opgeslagen als {filename}")


parser = argparse.ArgumentParser(description="Generate a high-resolution QR code.")
parser.add_argument("--data", required=True, help="The data to be included in the QR code (e.g., URL or WiFi info).")
parser.add_argument("--filename", default="qrcode.png", help="Filename for the QR code (default: qrcode.png)")
parser.add_argument("--version", type=int, default=10, help="QR code detail level (1-40, default: 10)")
parser.add_argument("--box_size", type=int, default=10, help="Size of each QR block in pixels (default: 10)")
parser.add_argument("--border", type=int, default=2, help="Thickness of the border in blocks (default: 2)")

args = parser.parse_args()

generate_qr(args.data, args.filename, args.version, args.box_size, args.border)
