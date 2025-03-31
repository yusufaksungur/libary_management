class Kitap:
    def __init__(self, kitapadi, yazaradi, sayfasayisi):
        self.kitapadi = kitapadi
        self.yazaradi = yazaradi
        self.sayfasayisi = sayfasayisi

    def bilgiler(self):
        return f"📖 Kitap Adı: {self.kitapadi}, ✍️ Yazar: {self.yazaradi}, 📄 Sayfa Sayısı: {self.sayfasayisi}"


class KitapYoneticisi:
    def __init__(self):
        self.kitaplar = []

    def kitap_ekle(self, kitapadi, yazaradi, sayfasayisi):
        """Yeni bir kitap ekler."""
        try:
            if not kitapadi or not yazaradi or sayfasayisi <= 0:
                raise ValueError("⚠️ Geçersiz kitap bilgileri!")

            yeni_kitap = Kitap(kitapadi, yazaradi, sayfasayisi)
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

    def kitap_sil(self, kitapadi):
        """Belirtilen kitabı siler."""
        for kitap in self.kitaplar:
            if kitap.kitapadi.lower() == kitapadi.lower():
                self.kitaplar.remove(kitap)
                print(f"🗑️ {kitapadi} adlı kitap silindi.")
                return
        print("⚠️ Belirtilen kitap bulunamadı!")

    def toplam_kitap_sayisi(self):
        """Toplam kitap sayısını döndürür."""
        return len(self.kitaplar)
