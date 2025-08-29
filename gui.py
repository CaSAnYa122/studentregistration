import tkinter as tk
from tkinter import messagebox
from database import register_student
def start_gui():
    root=tk.Tk()
    root.title("Student Registration")
    root.geometry("250x250")
    name_label=tk.Label(root,text="Name :")
    name_label.grid(row=0,column=0,padx=10,pady=10)
    name_entry=tk.Entry(root)
    name_entry.grid(row=0,column=1,padx=10,pady=10)
    email_label=tk.Label(root,text="Email :")
    email_label.grid(row=1,column=0,padx=10,pady=10)
    email_entry=tk.Entry(root)
    email_entry.grid(row=1,column=1,padx=10,pady=10)

    def submit():
        name=name_entry.get()
        email=email_entry.get()
        if name and email:
            try:
                register_student(name,email)
                messagebox.showinfo("Success!",
                                    "Student has been registered successfully")
            except Exception as e:
                messagebox.showerror("Error!",str(e))
            finally:
                name_entry.delete(0,tk.END)
                email_entry.delete(0,tk.END)
        

        else:
            messagebox.showwarning("Input Error!",
                                   "Please fill all the required fields")
    submit_button=tk.Button(root,text="Register",command=submit)
    submit_button.grid(row=2,column=0,columnspan=2,pady=20)
    root.mainloop()
