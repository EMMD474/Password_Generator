import string
import secrets
import customtkinter as c


def generate_password():
    try:
        display.delete("0.0", "end")
        length = int(entry.get())
        if length < 6:
            display.insert("0.0", "Password must not be less than six")
        else:
            chars: str = string.ascii_letters + string.digits + string.punctuation
            password: str = "".join(secrets.choice(chars) for _ in range(length))
            display.insert("0.0", f"Password: {password}")
    except ValueError:
        display.insert("0.0", "Length given is not a number")


def change_mode():
    if switch_var.get() == "off":
        c.set_appearance_mode("light")
    else:
        c.set_appearance_mode("dark")


c.set_appearance_mode("dark")
c.set_default_color_theme("green")

root = c.CTk()
root.geometry("400x310")

frame = c.CTkFrame(root)
frame.pack(pady=30, padx=40, fill="both", expand=True)

label = c.CTkLabel(frame, text="Password Generator", text_color=("#12002f", "teal"), font=("sans-serif", 16))
label.pack(pady=12, padx=10)

switch_var = c.StringVar(value="on")
switch = c.CTkSwitch(frame, text="Light / Dark mode", variable=switch_var, offvalue="off", onvalue="on"
                     , command=change_mode)
switch.pack()

entry = c.CTkEntry(frame, placeholder_text="Limit", width=140, height=26, font=("sans-serif", 12))
entry.pack(pady=10, padx=10)

button = c.CTkButton(frame, text="Generate Password", hover_color="#12002f", font=("sans-serif", 12),
                     command=generate_password)
button.pack(pady=12, padx=10)

display = c.CTkTextbox(frame, width=240, height=30, font=("sans-serif", 12), text_color=("#222", "#000"))
display.pack(pady=10, padx=10)

root.mainloop()
