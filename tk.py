import tkinter as tk

def submit():

    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    age = age_entry.get()
    city = city_entry.get()

    print("First Name:", first_name)
    print("Last Name:", last_name)
    print("Age:", age)
    print("City:", city)

window = tk.Tk()
window.title("Multiple Input Form")

first_name_label = tk.Label(window, text="First Name:")
first_name_label.grid(row=0, column=0)
first_name_entry = tk.Entry(window)
first_name_entry.grid(row=0, column=1)

last_name_label = tk.Label(window, text="Last Name:")
last_name_label.grid(row=1, column=0)
last_name_entry = tk.Entry(window)
last_name_entry.grid(row=1, column=1)

age_label = tk.Label(window, text="Age:")
age_label.grid(row=2, column=0)
age_entry = tk.Entry(window)
age_entry.grid(row=2, column=1)

city_label = tk.Label(window, text="City:")
city_label.grid(row=3, column=0)
city_entry = tk.Entry(window)
city_entry.grid(row=3, column=1)

submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.grid(row=4, columnspan=2)

window.mainloop()