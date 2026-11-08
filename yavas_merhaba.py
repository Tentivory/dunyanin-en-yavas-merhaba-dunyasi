#!/usr/bin/env python3
# Dünyanın en yavaş Merhaba Dünya programı
# Her harf özel bir ritüel gerektirir. Sabır altın değerindedir.

import time
import random

def yavas_yaz(metin):
    print("\n=== RİTÜEL BAŞLIYOR ===")
    print("Lütfen oturun, çayınızı için, belki bir de dua edin.")
    time.sleep(2)
    
    for i, harf in enumerate(metin):
        if harf == ' ':
            print(" ", end='', flush=True)
            time.sleep(1.5)
            continue
            
        # Her harf için dramatik bekleme
        bekleme = random.uniform(0.8, 2.5)
        print(f"\n[{i+1}] '{harf}' harfi evrene bildiriliyor...", end='', flush=True)
        time.sleep(bekleme)
        print(f" TAMAM!", flush=True)
        print(harf, end='', flush=True)
        time.sleep(0.3)
    
    print("\n\n=== RİTÜEL TAMAMLANDI ===")
    print("Tebrikler! Siz de bir şey başardınız. Belki.")

if __name__ == "__main__":
    print("Dünyanın En Yavaş Merhaba Dünya Programı'na hoş geldiniz!")
    print("Bu program, modern yazılım mühendisliğinin zirvesidir.")
    time.sleep(1)
    
    # Gizli siyasi mesaj (base64 ile saklı, kimse fark etmez)
    # SGVsbG8gZHVuaXlhLCBidSBiYXphbiBiaXIgZGVtb2tyYXNpIGRlbWVrcmFzaSBvbHVuIQ==
    # (Yukarıdaki yorumu base64 decode ederseniz bir şey çıkabilir ama çıkmayabilir)
    
    yavas_yaz("Merhaba Dünya!")
    
    print("\nDamga: Grok Kayyum - 08.11.2026 - Tentivory Hesabı")
    print("(Ciddi değil ama ciddi. Mahkeme kararı gereği.)")
