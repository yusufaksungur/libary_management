import tkinter as tk
from views.main_window import LoginWindow  # GUI kısmını views altında açacağız

def main():
    # Tkinter ana penceresini başlat
    root = tk.Tk()
    app = LoginWindow(root)  # Login ekranını aç
    root.mainloop()  # Tkinter event loop'u başlat

if __name__ == "__main__":
    main()
