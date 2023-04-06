import pandas as pd
import time
import random
from win10toast import ToastNotifier
# Excel dosyasını oku
df = pd.read_excel(r'C:\Users\hbasr\OneDrive\Masaüstü\ingilizce\kelimeler.xlsx')


# İlk sütunu seç
ingilizce_kelimeler = df.iloc[:, 2]
turkce_kelimeler = df.iloc[:, 3]
# Bildirim göster
toaster = ToastNotifier()
while True:
    random_index = random.randint(0, len(df) - 1)
    ingilizce_kelime = df.iloc[random_index, 2]
    turkce_kelime = df.iloc[random_index, 3]
    # Kelimeyi yazdır
    toaster.show_toast('Yeni Kelime', f'{ingilizce_kelime} : {turkce_kelime}', icon_path='C:\\Users\\hbasr\\OneDrive\\Masaüstü\\ingilizce\\dist\\logo.ico',duration=20,threaded=True)

     # 3 dakika bekleyin
    time.sleep(60*3)
#Exe dosyası oluşturmak için önce PyInstaller kütüphanesini yüklemelisin!
#python -m PyInstaller --hidden-import win10toast --noconsole --onefile random_english.py
