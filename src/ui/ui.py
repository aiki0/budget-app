import tkinter as tk
from tkinter import messagebox

def start_ui(service):
    root = tk.Tk()
    root.title("Budjettisovellus")
    root.geometry("450x600")

    def clear_window():
        for widget in root.winfo_children():
            widget.destroy()

    def show_login():
        clear_window()

        tk.Label(master=root, text="Kirjaudu tai rekisteröidy").pack()

        tk.Label(master=root, text="Käyttäjätunnus:").pack()
        username_entry = tk.Entry(master=root)
        username_entry.pack()

        tk.Label(master=root, text="Salasana:").pack()
        password_entry = tk.Entry(master=root, show="*")
        password_entry.pack()

        def handle_login():
            username = username_entry.get()
            password = password_entry.get()
            
            if service.login(username, password):
                show_main()
            else:
                messagebox.showerror("Virhe", "Väärä tunnus tai salasana.")

        def handle_register():
            username = username_entry.get()
            password = password_entry.get()
            
            if not username or not password:
                messagebox.showerror("Virhe", "Täytä molemmat kentät!")
                return
                
            if service.register(username, password):
                messagebox.showinfo("Onnistui", "Tunnus luotu! Voit nyt kirjautua.")
            else:
                messagebox.showerror("Virhe", "Tunnus on jo varattu.")

        tk.Button(master=root, text="Kirjaudu", command=handle_login).pack()
        tk.Button(master=root, text="Rekisteröidy", command=handle_register).pack()


    def show_main():
        clear_window()

        def update_list():
            expense_listbox.delete(0, tk.END)
            expenses = service.get_all()

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
                service.add_expense(amount, category_input)
                amount_entry.delete(0, tk.END)
                category_entry.delete(0, tk.END)
                update_list()
            except ValueError:
                messagebox.showerror("Virhe", "Syötä määrä numerona.")

        def handle_delete_expense():
            selection = expense_listbox.curselection()
            
            if not selection:
                messagebox.showinfo("Huom", "Valitse poistettava kulu listasta.")
                return
            index = selection[0]
            expenses = service.get_all()
            expense_id = expenses[index]["id"]
            
            service.delete_expense(expense_id)
            update_list()
        def handle_edit_expense():
                    selection = expense_listbox.curselection()
                    if not selection:
                        messagebox.showinfo("Huom", "Valitse muokattava kulu listasta.")
                        return

                    index = selection[0]
                    expenses = service.get_all()
                    selected_expense = expenses[index]

                    edit_window = tk.Toplevel(root)
                    edit_window.title("Muokkaa kulua")
                    edit_window.geometry("300x250")

                    tk.Label(master=edit_window, text="Uusi kulu €:").pack()
                    new_amount_entry = tk.Entry(master=edit_window)
                    new_amount_entry.insert(0, str(selected_expense["amount"]))
                    new_amount_entry.pack()

                    tk.Label(master=edit_window, text="Uusi kategoria:").pack()
                    new_category_entry = tk.Entry(master=edit_window)
                    new_category_entry.insert(0, selected_expense["category"])
                    new_category_entry.pack()

                    def save_edit():
                        new_category = new_category_entry.get()
                        try:
                            new_amount = int(new_amount_entry.get())
                            service.edit_expense(selected_expense["id"], new_amount, new_category)
                            
                            update_list()
                            edit_window.destroy()
                        except ValueError:
                            messagebox.showerror("Virhe", "Syötä määrä numerona.", parent=edit_window)

                    tk.Button(master=edit_window, text="Tallenna muutokset", command=save_edit).pack()


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

        add_button = tk.Button(master=root, text="Tallenna kulu", command=handle_add_expense)
        add_button.pack()

        delete_button = tk.Button(master=root, text="Poista kulu", command=handle_delete_expense)
        delete_button.pack()

        edit_button = tk.Button(master=root, text="Muokkaa valittua", command=handle_edit_expense)
        edit_button.pack()

        expense_listbox = tk.Listbox(master=root)
        expense_listbox.pack()

        update_list()

    show_login()
    root.mainloop()