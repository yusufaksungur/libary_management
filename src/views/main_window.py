import tkinter as tk
from tkinter import messagebox
from controllers.user_controller import Admin
from controllers.book_controller import KitapYoneticisi

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Girişi")
        self.root.geometry("300x200")
        
        self.admin = Admin()
        
        tk.Label(self.root, text="Kullanıcı Adı:").pack()
        self.entry_username = tk.Entry(self.root)
        self.entry_username.pack()
        
        tk.Label(self.root, text="Şifre:").pack()
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack()
        
        tk.Button(self.root, text="Giriş Yap", command=self.login).pack(pady=10)
    
    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        
        if self.admin.girisyap(username, password):
            self.root.destroy()
            self.open_book_window()
        else:
            messagebox.showerror("Hata", "Geçersiz kullanıcı adı veya şifre!")
    
    def open_book_window(self):
        new_root = tk.Tk()
        BookWindow(new_root)  # Kitap yönetimi penceresini başlat
        new_root.mainloop()

class BookWindow:
    def __init__(self, root):
        self.yonetici = KitapYoneticisi()
        self.root = root
        self.root.title("Kütüphane Yönetim Sistemi")
        self.root.geometry("500x500")
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)
        
        self.entry_kitapadi = tk.Entry(self.frame, width=20)
        self.entry_kitapadi.grid(row=0, column=1)
        tk.Label(self.frame, text="Kitap Adı:").grid(row=0, column=0)
        
        self.entry_yazaradi = tk.Entry(self.frame, width=20)
        self.entry_yazaradi.grid(row=1, column=1)
        tk.Label(self.frame, text="Yazar Adı:").grid(row=1, column=0)
        
        self.entry_sayfa = tk.Entry(self.frame, width=20)
        self.entry_sayfa.grid(row=2, column=1)
        tk.Label(self.frame, text="Sayfa Sayısı:").grid(row=2, column=0)
        
        self.entry_yayinevi = tk.Entry(self.frame, width=20)
        self.entry_yayinevi.grid(row=3, column=1)
        tk.Label(self.frame, text="Yayınevi:").grid(row=3, column=0)
        
        self.entry_raf = tk.Entry(self.frame, width=20)
        self.entry_raf.grid(row=4, column=1)
        tk.Label(self.frame, text="Raf No:").grid(row=4, column=0)
        
        tk.Button(self.root, text="Kitap Ekle", command=self.ekle).pack()
        
        self.listbox = tk.Listbox(self.root, width=50)
        self.listbox.pack(pady=10)
        
        tk.Button(self.root, text="Kitap Sil", command=self.sil).pack()
        
        self.listele()
    
    def ekle(self):
        try:
            sayfa_sayisi = int(self.entry_sayfa.get())
            if sayfa_sayisi <= 0:
                raise ValueError("Sayfa sayısı pozitif olmalıdır.")
            self.yonetici.kitap_ekle(
                self.entry_kitapadi.get(), self.entry_yazaradi.get(), sayfa_sayisi,
                self.entry_yayinevi.get(), self.entry_raf.get()
            )
            self.listele()
        except ValueError as e:
            messagebox.showerror("Hata", str(e))
    
    def sil(self):
        secili = self.listbox.curselection()
        if secili:
            kitapadi = self.listbox.get(secili[0]).split(" - ")[0]
            self.yonetici.kitap_sil(kitapadi)
            self.listele()
    
    def listele(self):
        self.listbox.delete(0, tk.END)
        for kitap in self.yonetici.kitaplar:
            self.listbox.insert(tk.END, kitap.bilgiler())
