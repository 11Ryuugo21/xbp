import serial
import qrcode

# Arduinoと接続
ser = serial.Serial('COM3', 9600)  # COMポートは適切に設定

def get_uv_index():
    if ser.in_waiting > 0:
        uv_index = ser.readline().decode('utf-8').strip()
        return uv_index
    return None

def generate_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save("uv_index_qr.png")

while True:
    uv_index = get_uv_index()
    if uv_index:
        print(f"Current UV Index: {uv_index}")
        generate_qr(uv_index)
