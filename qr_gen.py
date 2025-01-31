import qrcode
import argparse


def generate_qr(data, filename="qrcode.png", version=10, box_size=10, border=2):
    """Genereert een gedetailleerde QR-code en slaat deze op als PNG-afbeelding."""
    qr = qrcode.QRCode(
        version=version,  # Hoe hoger het getal, hoe meer details (1-40)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # H = hoogste foutcorrectie
        box_size=box_size,  # Pixels per QR-blokje (hogere waarde = hogere resolutie)
        border=border,  # Randgrootte in blokken
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"✅ QR-code opgeslagen als {filename}")


# Command-line argumenten parser
parser = argparse.ArgumentParser(description="Genereer een QR-code met hoge resolutie.")
parser.add_argument("--data", required=True, help="De data die in de QR-code moet komen (bijv. URL of WiFi-info).")
parser.add_argument("--filename", default="qrcode.png", help="Bestandsnaam voor de QR-code (default: qrcode.png)")
parser.add_argument("--version", type=int, default=10, help="Detailniveau van de QR-code (1-40, default: 10)")
parser.add_argument("--box_size", type=int, default=10, help="Grootte van elk QR-blokje in pixels (default: 10)")
parser.add_argument("--border", type=int, default=2, help="Dikte van de rand in blokken (default: 2)")
args = parser.parse_args()

# QR-code genereren met variabele invoer
generate_qr(args.data, args.filename, args.version, args.box_size, args.border)
