import pyautogui
import time
import random
import pandas as pd
import tkinter as tk
from tkinter import messagebox

def show_popup(message, duration=20):
    popup_width = 400
    popup_height = 100
    root = tk.Tk()
    root.title('Yeni Kelime')
    #Pop-up'ı ekran çözünürlüğüne göre sağ alta alma
    root.geometry(f'{popup_width}x{popup_height}+{root.winfo_screenwidth()-popup_width-10}+{root.winfo_screenheight()-popup_height-70}')
    font = ('Helvetica', 20, 'bold', 'italic', 'underline')
    label = tk.Label(root, text=message , font=font)
    label.pack(pady=20)
    root.after(duration*1000, root.destroy) # duration saniye sonra kapat
    root.mainloop()
# Excel dosyasını oku
df = pd.read_excel(r'C:\Users\hbasr\OneDrive\Masaüstü\ingilizce\kelimeler.xlsx')

# İlk sütunu seç
ingilizce_kelimeler = df.iloc[:, 2]
turkce_kelimeler = df.iloc[:, 3]

while True:
    random_index = random.randint(0, len(df) - 1)
    ingilizce_kelime = df.iloc[random_index, 2]
    turkce_kelime = df.iloc[random_index, 3]
    
    # Bildirim mesajı oluştur
    message = f'{ingilizce_kelime} : {turkce_kelime}'
    
    # Mesajı göster
    show_popup(message)
    
    # 15 dakika bekleyin
    time.sleep(5*60)


#Exe dosyası oluşturmak için önce PyInstaller kütüphanesini yüklemelisin!
#python -m PyInstaller --hidden-import win10toast --noconsole --onefile eng-tr-reminder.py
