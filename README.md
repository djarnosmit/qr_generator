# QR Code Generator 🖼️📲

A simple and flexible Python script to generate high-resolution QR codes for various data types, including URLs, WiFi access points, GPS coordinates, and more.

## 🚀 Features
✅ Supports **custom QR data** (e.g., URLs, WiFi credentials, addresses, etc.)  
✅ Allows **adjustable resolution**, border size, and error correction level  
✅ Generates **high-resolution PNG QR codes**  
✅ Uses **default values** if parameters are not provided  

## 📦 Installation

### 🔹 Install dependencies with `requirements.txt`
First, create a **virtual environment** (recommended):

```bash
python -m venv .venv

Activate the virtual environment:

    macOS/Linux:

source .venv/bin/activate

Windows (cmd):

.venv\Scripts\activate

Windows (PowerShell):

    .venv\Scripts\Activate.ps1

Now install the required packages from requirements.txt:

pip install -r requirements.txt

📦 Alternative: Install dependencies manually

If you prefer, you can install the required packages manually:

pip install qrcode[pil]

🔧 Usage

Run the script with default settings:

python qr_generator.py --data "https://guestwifi.example.com/login"

🎯 Custom Parameters

You can specify additional parameters to customize the QR code:

python qr_generator.py --data "https://guestwifi.example.com/login" \
  --filename "custom_qr.png" \
  --version 15 \
  --box_size 20 \
  --border 4

📌 Parameter Explanations
Parameter	Description	Default Value
--data	The content to be encoded in the QR code	Required
--filename	The output file name for the QR code image	qrcode.png
--version	QR detail level (1-40, higher = more complex QR)	10
--box_size	Size of each QR block (higher = higher resolution)	10
--border	Border size around the QR code in blocks	2
🔥 Examples

Generate a WiFi QR code for easy network access:

python qr_generator.py --data "WIFI:T:WPA;S=GuestNetwork;P=GuestPassword;;" --filename "wifi_qr.png"

Generate a GPS location QR code:

python qr_generator.py --data "geo:52.3702,4.8952" --filename "gps_qr.png"

🛠️ Updating Dependencies

If new dependencies are added, update requirements.txt:

pip freeze > requirements.txt

📄 License

This project is licensed under the MIT License – feel free to modify and use it as needed.


---

### ✅ **Wat is er nieuw?**
- **Toegevoegd:** Installatie-instructies met `requirements.txt`
- **Toegevoegd:** Hoe je de **dependencies bijwerkt** (`pip freeze > requirements.txt`)
- **Duidelijkere structuur** voor installatie en gebruik  

Nu is je **README.md** volledig **Git-ready**! 🚀💡 Laat weten als je nog aanpassingen wilt! 😃

