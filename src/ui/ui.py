import tkinter as tk
from tkinter import messagebox

def start_ui(service):
    root = tk.Tk()
    root.title("Budjettisovellus")
    root.geometry("450x600")

    def update_list():
        expense_listbox.delete(0, tk.END)
        expenses = service.hae_kaikki()

        for expense in expenses:
            expense_listbox.insert(tk.END, f"{expense['category']}: {expense['amount']}€")

    def handle_add_expense():
        amount_input = amount_entry.get()
        category_input = category_entry.get()

        if not amount_input:
            messagebox.showerror("Virhe", "Määrä ei voi olla tyhjä!")
            return
        try:
            amount = int(amount_input)
            service.lisaa_kulu(amount, category_input)
            amount_entry.delete(0, tk.END)
            category_entry.delete(0, tk.END)
            update_list()
        except ValueError:
            messagebox.showerror("Virhe", "Syötä määrä numerona.")


    title_label = tk.Label(master=root, text="Lisää uusi kulu")
    title_label.pack()

    amount_label = tk.Label(master=root, text="Kulu €:")
    amount_label.pack()
    amount_entry = tk.Entry(master=root)
    amount_entry.pack()

    category_label = tk.Label(master=root, text="Kategoria:")
    category_label.pack()
    category_entry = tk.Entry(master=root)
    category_entry.pack()

    add_button = tk.Button(master=root, text="Tallenna kulu",command=handle_add_expense)
    add_button.pack()

    expense_listbox = tk.Listbox(master=root)
    expense_listbox.pack()

    update_list()
    root.mainloop()