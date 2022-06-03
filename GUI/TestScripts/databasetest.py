from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title("Parker's Test App")
root.geometry("400x600")

# Databases

# Create a db / connect to one
conn = sqlite3.connect("address_book.db")

# Create cursor
c = conn.cursor()

# Create Table
'''
c.execute(
    """CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        province text,
        zipcode integer
        )"""
)
'''

# Create submit function for DB
def submit():
    # Create a db / connect to one
    conn = sqlite3.connect("address_book.db")
    # Create cursor
    c = conn.cursor()

    # Insert into Table
    c.execute(
        "INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :province, :zipcode)",
        {
            "f_name": f_name.get(),
            "l_name": l_name.get(),
            "address": address.get(),
            "city": city.get(),
            "province": province.get(),
            "zipcode": zipcode.get(),
        },
    )

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

    # Clear the textboxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    province.delete(0, END)
    zipcode.delete(0, END)


# Create Query Function
def query():
    # Create a db / connect to one
    conn = sqlite3.connect("address_book.db")
    # Create cursor
    c = conn.cursor()

    # Query the Database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    # print(records)

    # Loop through results
    print_records = ""
    for record in records:
        print_records += (
            str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"
        )

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()


# Create Function to Delete a Record
def delete():
    # Create a db / connect to one
    conn = sqlite3.connect("address_book.db")
    # Create cursor
    c = conn.cursor()

    # Delete a Record
    c.execute("DELETE from addresses WHERE oid= " + delete_box.get())

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()


# Create Function to Edit / Update a Record
def edit():
    editor = Tk()
    editor.title("Parker's Test App")
    editor.geometry("400x600")

    # Create a db / connect to one
    conn = sqlite3.connect("address_book.db")
    # Create cursor
    c = conn.cursor()

    # Query the Database
    c.execute("SELECT * FROM addresses")
    records = c.fetchall()
    # print(records)

    # Loop through results
    print_records = ""
    for record in records:
        print_records += (
            str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"
        )

    # Create Text Boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)
    province_editor = Entry(editor, width=30)
    province_editor.grid(row=4, column=1, padx=20)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)

    # Create Text Box Labels
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)
    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)
    province_label = Label(editor, text="Province")
    province_label.grid(row=4, column=0)
    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0)

    # Create a Save Button to save edited Records
    save_btn = Button(editor, text="Save Record", command=edit)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=20, ipadx=137)


# Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
province = Entry(root, width=30)
province.grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# Create Text Box Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
province_label = Label(root, text="Province")
province_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)
delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=9, column=0, pady=5)

# Create Submit Buttons
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=20, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=20, ipadx=127)

# Create a Delete Button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=20, ipadx=130)

# Create an Update Button
edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=20, ipadx=137)

# Commit changes
conn.commit()

# Close connection
conn.close()

root.mainloop()
