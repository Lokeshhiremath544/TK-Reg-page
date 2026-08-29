import tkinter as tk
from tkinter import messagebox


class RegistrationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Form")
        self.root.geometry("420x520")
        self.root.resizable(False, False)
        self.root.configure(bg="#f2f2f2")

        self.title_label = tk.Label(
            root,
            text="Create an Account",
            font=("Arial", 20, "bold"),
            bg="#f2f2f2",
            fg="#222222",
            pady=20,
        )
        self.title_label.pack()

        self.form_frame = tk.Frame(root, bg="#f2f2f2")
        self.form_frame.pack(padx=25, pady=(0, 20), fill="x")

        self.fields = {
            "Full Name": ("full_name", "Enter full name"),
            "Email": ("email", "Enter email address"),
            "Username": ("username", "Choose a username"),
            "Password": ("password", "Enter password"),
            "Confirm Password": ("confirm_password", "Confirm password"),
        }

        self.entries = {}

        for label_text, (key, placeholder) in self.fields.items():
            label = tk.Label(
                self.form_frame,
                text=label_text,
                font=("Arial", 11, "bold"),
                bg="#f2f2f2",
                anchor="w",
            )
            label.pack(fill="x", pady=(8, 4))

            entry = tk.Entry(
                self.form_frame,
                width=40,
                font=("Arial", 11),
                show="*" if "Password" in label_text else "",
            )
            entry.insert(0, placeholder) if "Password" not in label_text else None
            entry.pack(fill="x", pady=(0, 8))
            self.entries[key] = entry

        self.register_button = tk.Button(
            root,
            text="Register",
            width=24,
            height=2,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 11, "bold"),
            command=self.register,
            relief="flat",
            cursor="hand2",
        )
        self.register_button.pack(pady=10)

        self.login_label = tk.Label(
            root,
            text="Already have an account? Login",
            fg="#0078d7",
            bg="#f2f2f2",
            cursor="hand2",
            font=("Arial", 10),
        )
        self.login_label.pack()
        self.login_label.bind("<Button-1>", lambda e: messagebox.showinfo("Login", "Login page coming soon!"))

    def register(self):
        full_name = self.entries["full_name"].get().strip()
        email = self.entries["email"].get().strip()
        username = self.entries["username"].get().strip()
        password = self.entries["password"].get()
        confirm_password = self.entries["confirm_password"].get()

        if not all([full_name, email, username, password, confirm_password]):
            messagebox.showerror("Missing Fields", "Please complete all fields.")
            return

        if "@" not in email or "." not in email:
            messagebox.showerror("Invalid Email", "Please enter a valid email address.")
            return

        if len(password) < 6:
            messagebox.showerror("Weak Password", "Password must be at least 6 characters long.")
            return

        if password != confirm_password:
            messagebox.showerror("Password Mismatch", "Passwords do not match.")
            return

        messagebox.showinfo(
            "Registration Successful",
            f"Welcome, {full_name}!\nYour account '{username}' has been created successfully."
        )

        for entry in self.entries.values():
            entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationApp(root)
    root.mainloop()
