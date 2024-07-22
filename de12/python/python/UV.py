import serial
import tkinter as tk
from tkinter import ttk

# シリアルポートの設定（適切なポートに変更してください）
SERIAL_PORT = 'COM3'
BAUD_RATE = 9600

class UVCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("UVチェッカー")
        
        self.label = ttk.Label(root, text="UVセンサーデータ:", font=("Arial", 16))
        self.label.pack(pady=20)
        
        self.data_label = ttk.Label(root, text="--", font=("Arial", 24))
        self.data_label.pack(pady=20)
        
        self.serial_connection = serial.Serial(SERIAL_PORT, BAUD_RATE)
        self.update_data()

    def update_data(self):
        if self.serial_connection.in_waiting > 0:
            uv_data = self.serial_connection.readline().decode('utf-8').strip()
            self.data_label.config(text=uv_data)
            self.data_label.config(text=uv_data)
        
        self.root.after(1000, self.update_data)

def main():
    root = tk.Tk()
    app = UVCheckerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()