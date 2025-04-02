import tkinter as tk
from tkinter import ttk, messagebox
from controllers.user_controller import Admin
from controllers.book_controller import KitapYoneticisi

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Girişi")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        
        self.admin = Admin()
        
        frame = ttk.Frame(self.root, padding=10)
        frame.pack(expand=True)
        
        ttk.Label(frame, text="Kullanıcı Adı:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.entry_username = ttk.Entry(frame)
        self.entry_username.grid(row=0, column=1, pady=5)
        
        ttk.Label(frame, text="Şifre:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.entry_password = ttk.Entry(frame, show="*")
        self.entry_password.grid(row=1, column=1, pady=5)
        
        ttk.Button(frame, text="Giriş Yap", command=self.login).grid(row=2, column=0, columnspan=2, pady=10)
    
    def login(self):
        username = self.entry_username.get().strip()
        password = self.entry_password.get().strip()
        
        if self.admin.girisyap(username, password):
            self.root.destroy()
            self.open_book_window()
        else:
            messagebox.showerror("Hata", "Geçersiz kullanıcı adı veya şifre!")
    
    def open_book_window(self):
        new_root = tk.Tk()
        BookWindow(new_root)
        new_root.mainloop()

class BookWindow:
    def __init__(self, root):
        self.yonetici = KitapYoneticisi()
        self.root = root
        self.root.title("Kütüphane Yönetim Sistemi")
        self.root.geometry("500x500")
        
        frame = ttk.Frame(self.root, padding=10)
        frame.pack(pady=10)
        
        self.entry_kitapadi = self.create_entry(frame, "Kitap Adı:", 0)
        self.entry_yazaradi = self.create_entry(frame, "Yazar Adı:", 1)
        self.entry_sayfa = self.create_entry(frame, "Sayfa Sayısı:", 2)
        self.entry_yayinevi = self.create_entry(frame, "Yayınevi:", 3)
        self.entry_raf = self.create_entry(frame, "Raf No:", 4)
        
        ttk.Button(self.root, text="Kitap Ekle", command=self.ekle).pack(pady=5)
        
        self.listbox = tk.Listbox(self.root, width=50, height=10)
        self.listbox.pack(pady=10)
        
        ttk.Button(self.root, text="Kitap Sil", command=self.sil).pack()
        
        self.listele()
    
    def create_entry(self, parent, label_text, row):
        ttk.Label(parent, text=label_text).grid(row=row, column=0, sticky=tk.W, pady=2)
        entry = ttk.Entry(parent, width=25)
        entry.grid(row=row, column=1, pady=2)
        return entry
    
    def ekle(self):
        try:
            sayfa_sayisi = int(self.entry_sayfa.get().strip())
            if sayfa_sayisi <= 0:
                raise ValueError("Sayfa sayısı pozitif olmalıdır.")
            
            self.yonetici.kitap_ekle(
                self.entry_kitapadi.get().strip(),
                self.entry_yazaradi.get().strip(),
                sayfa_sayisi,
                self.entry_yayinevi.get().strip(),
                self.entry_raf.get().strip()
            )
            self.listele()
        except ValueError as e:
            messagebox.showerror("Hata", str(e))
    
    def sil(self):
        secili = self.listbox.curselection()
        
        if not secili:  
            messagebox.showwarning("Uyarı", "Lütfen silmek için bir kitap seçin!")
            return

        kitap_bilgisi = self.listbox.get(secili[0])  
        print(f"🔎 Seçili Kitap: {kitap_bilgisi}")  

        if not kitap_bilgisi:
            messagebox.showerror("Hata", "Seçili kitap bilgisi boş!")
            return

        kitap_adi = kitap_bilgisi.split(" - ")[0].strip()  

        if messagebox.askyesno("Onay", f"'{kitap_adi}' adlı kitabı silmek istediğinize emin misiniz?"):
            self.yonetici.kitap_sil(kitap_adi)  # Kitabı listeden çıkar
            self.listele()  # Listbox'u güncelle


    
    def listele(self):
        self.listbox.delete(0, tk.END)  # Önce listeyi temizle
        for kitap in self.yonetici.kitaplar:  
            self.listbox.insert(tk.END, kitap.bilgiler())  # Güncellenmiş listeyi ekle


if __name__ == "__main__":
    root = tk.Tk()
    LoginWindow(root)
    root.mainloop()
