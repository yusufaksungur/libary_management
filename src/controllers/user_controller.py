import hashlib

class Admin:
    def __init__(self):
        self.admin_name = "a"
        self.admin_password = hashlib.sha256("a1".encode()).hexdigest()
        
    def sifrele(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def girisyap(self, name, password):
        if name == self.admin_name and self.sifrele(password) == self.admin_password:
            print("✅ Giriş başarılı!")
            return True
        else:
            print("⚠️ Hatalı kullanıcı adı veya şifre!")
            return False
