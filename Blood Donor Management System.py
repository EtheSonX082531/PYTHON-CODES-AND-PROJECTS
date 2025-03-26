import tkinter as tk
from tkinter import messagebox, simpledialog
import random

Donor_list = []

class Blood_donor:
    def __init__(self, name, age, place, group, contact_no):
        self.name = name
        self.age = age
        self.place = place
        self.group = group
        self.contact_no = contact_no
        Donor_list.append(self)

d1 = Blood_donor("Priyanto Chandra Dey", 22, "Sylhet", "O+", "01744XXXXXX")  
d2 = Blood_donor("Tamim Amin Suhag", 21, "Sylhet", "O+", "01922XXXXXX")   
d3 = Blood_donor("Dhiraj Dhar Dip", 24, "Comilla", "A+", "01891XXXXXX")    
d4 = Blood_donor("Md Mutahar Mahmud Chy", 21, "Barishal", "AB+", "01777XXXXXX")
d5 = Blood_donor("Anik Roy", 22, "Sylhet", "O+", "01734XXXXXX") 
d6 = Blood_donor("Progga Dey Troyee",20,"Rangpur","O-","01932XXXXXX")

def find_nearest_donor():
    receiver_group = simpledialog.askstring("Input", "Enter Patient group:")
    receiver_place = simpledialog.askstring("Input", "Enter Patient's place:")
    
    NewList1 = []
    NewList2 = []
    
    for el in Donor_list:
        if el.group == receiver_group:
            if el.place == receiver_place:
                NewList1.append(el)
            else:
                NewList2.append(el)
    
    if NewList1:
        donor = random.choice(NewList1)
        messagebox.showinfo("Nearest match found", f"Name: {donor.name}\nAge: {donor.age}\nPlace: {donor.place}\nGroup: {donor.group}\nContact No: {donor.contact_no}")
    elif NewList2:
        details = "We have no nearest blood donor in our list\nBut we have some donors for you\n\n"
        for el in NewList2:
            details += f"Name: {el.name}\nAge: {el.age}\nPlace: {el.place}\nGroup: {el.group}\nContact No: {el.contact_no}\n\n"
        messagebox.showinfo("Other donors found", details)
    else:
        messagebox.showinfo("No donor found", "Sorry! We have no donor for you.")

def add_new_donor():
    new_name = simpledialog.askstring("Input", "New donor name:")
    new_age = simpledialog.askinteger("Input", "New donor age:")
    new_place = simpledialog.askstring("Input", "New donor place:")
    new_group = simpledialog.askstring("Input", "New donor group:")
    new_contact_no = simpledialog.askstring("Input", "New donor Contact No:")
    newdonor = Blood_donor(new_name, new_age, new_place, new_group, new_contact_no)
    messagebox.showinfo("Success", "New donor added successfully!")

def see_all_donors():
    details = "Here are all the donors from the list:\n\n"
    for donor in Donor_list:
        details += f"Name: {donor.name}\nAge: {donor.age}\nPlace: {donor.place}\nBlood Group: {donor.group}\nContact No: {donor.contact_no}\n\n"
    messagebox.showinfo("All donors", details)

def search_placewise_donor():
    Search_place = simpledialog.askstring("Input", "Enter place name:")
    details = f"Blood donors in {Search_place}:\n\n"
    for donor in Donor_list:
        if donor.place == Search_place:
            details += f"Name: {donor.name}\nAge: {donor.age}\nPlace: {donor.place}\nBlood Group: {donor.group}\nContact No: {donor.contact_no}\n\n"
    if details == f"Blood donors in {Search_place}:\n\n":
        details = f"No donors found in {Search_place}."
    messagebox.showinfo(f"Donors in {Search_place}", details)

def search_groupwise_donor():
    Search_group = simpledialog.askstring("Input", "Enter Blood-Group:")
    details = f"Blood donors with {Search_group} group:\n\n"
    for donor in Donor_list:
        if donor.group == Search_group:
            details += f"Name: {donor.name}\nAge: {donor.age}\nPlace: {donor.place}\nBlood Group: {donor.group}\nContact No: {donor.contact_no}\n\n"
    if details == f"Blood donors with {Search_group} group:\n\n":
        details = f"No donors found with {Search_group} group."
    messagebox.showinfo(f"Donors with {Search_group}", details)

def exit_console():
    root.destroy()

root = tk.Tk()
root.title("Blood Donor Management System")

tk.Label(root, text="Blood Donor Management System", font=("BOLD", 16)).pack(pady=10)
tk.Label(root,text="Created by Anik Roy and Mahan Roy\n\n",font=("Helvetica",10)).pack(pady=5)

tk.Button(root, text="Find Nearest Blood Donor", command=find_nearest_donor).pack(pady=5)
tk.Button(root, text="Add New Donor", command=add_new_donor).pack(pady=5)
tk.Button(root, text="See All Donors", command=see_all_donors).pack(pady=5)
tk.Button(root, text="Search Placewise Blood Donor", command=search_placewise_donor).pack(pady=5)
tk.Button(root, text="Search Groupwise Blood Donor", command=search_groupwise_donor).pack(pady=5)
tk.Button(root, text="Exit", command=exit_console).pack(pady=5)

root.mainloop()
