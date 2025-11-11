import tkinter as t
from tkinter import StringVar

root=tk.Tk()
root.title("Kelas")
root.geometry("180x200")

def submit_form():
    kelas = selected_kelas.get()

    result_label.config(
        text = f"Kelas :- {kelas}\n"
    )

selected_kelas = StringVar()
selected_kelas.set("X")

kelas_frame = tk.Frame(root)
kelas_frame.grid(row=0, column=1, padx=10, pady=5)

tk.Radiobutton(kelas_frame, text=10, variable=selected_kelas, value="X").pack(side="left")
tk.Radiobutton(kelas_frame, text=11, variable=selected_kelas, value="XI").pack(side="left")
tk.Radiobutton(kelas_frame, text=12, variable=selected_kelas, value="XII").pack(side="left")

result_label = tk.Label(root, text="", font=("Arial", 10), fg="green")
result_label.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

tk.Button(root, text="SUBMIT", font=("Arial", 10), command=submit_form).grid(row=8, column=1, pady=10)


root.mainloop()
