import hashlib

class Admin:
    
    def __init__(self, name, password):
        self.admin_name = "admin"
        self.admin_password = "admin123"
        
    def sifrele(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def girisyap(self, name, password):
        if name == self.admin_name and self.sifrele(password) == self.sifrele(self.admin_password):
            print("✅ Giriş başarılı!")
            return True
        else:
            print("⚠️ Hatalı kullanıcı adı veya şifre!")
            return False
        