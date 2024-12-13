import tkinter as tk

root = tk.Tk()
name = "Louie_Macabuhay"
section = "BSIT-2A"
root.title(f"OOP LA29 {name}")
root.geometry("400x300")
root.configure(bg="black")

label = tk.Label(text=f"OOP LA29 {name} {section}")
label.grid(row=0, column=0, padx=100, pady=130)


root.mainloop()
