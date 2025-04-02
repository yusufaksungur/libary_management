class Kitap:
    def __init__(self, kitapadi, yazaradi, sayfasayisi, yayinevi, raf_no):
        self.kitapadi = kitapadi
        self.yazaradi = yazaradi
        self.sayfasayisi = sayfasayisi
        self.yayinevi = yayinevi
        self.raf_no = raf_no
        

    def bilgiler(self):
        return f"📖 Kitap Adı: {self.kitapadi}, ✍️ Yazar: {self.yazaradi}, 📄 Sayfa Sayısı: {self.sayfasayisi}, Yayınevi: {self.yayinevi}, Raf Numarası: {self.raf_no}"


class KitapYoneticisi:
    def __init__(self):
        self.kitaplar = []

    def kitap_ekle(self, kitapadi, yazaradi, sayfasayisi, yayinevi, raf_no):
        """Yeni bir kitap ekler."""
        try:
            if not kitapadi or not yazaradi or sayfasayisi  <= 0:
                raise ValueError("⚠️ Geçersiz kitap bilgileri!")

            yeni_kitap = Kitap(kitapadi, yazaradi, sayfasayisi, yayinevi, raf_no)
            self.kitaplar.append(yeni_kitap)
            print(f"✅ {kitapadi} adlı kitap başarıyla eklendi!")
        except ValueError as e:
            print(e)

    def kitaplari_listele(self):
        """Tüm kitapları listeler."""
        if not self.kitaplar:
            print("📭 Kütüphanede kitap bulunmamaktadır.")
        else:
            print("\n📚 Kütüphanedeki Kitaplar:")
            for kitap in self.kitaplar:
                print(kitap.bilgiler())
                
    def kitap_bul(self, kitapadi):
        for kitap in self.kitaplar:
            if kitap.kitapadi.lower() == kitapadi.lower():
                print(f"📖 Kitap Bulundu: {kitap.bilgiler()}")
                return
        print("⚠️ Belirtilen kitap bulunamadı!")

    def kitap_sil(self, kitapadi):
        
        bulunan_kitap = None
        for kitap in self.kitaplar:
            if kitap.kitapadi.lower() == kitapadi.lower():
                bulunan_kitap = kitap
                break  # İlk eşleşen kitabı bul ve çık
        
        if bulunan_kitap:
            self.kitaplar.remove(bulunan_kitap)
            print(f"🗑️ {kitapadi} adlı kitap silindi.")
        else:
            print("⚠️ Belirtilen kitap bulunamadı!")


    def toplam_kitap_sayisi(self):
        """Toplam kitap sayısını döndürür."""
        return len(self.kitaplar)
