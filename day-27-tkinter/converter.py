from tkinter import *

def convert_miles_to_km():
    miles = float(input.get())
    convertion_rate = 1.609344

    km = round(miles * convertion_rate)

    output.config(text=f"{km} Km")

# Window config
window = Tk()
window.title("Mile to Km Converter")
window.minsize(height=300, width=300)
window.config(padx=20, pady=20)

# Entry
input = Entry(width=10)
input.grid(column=1, row=0)
input.insert(0, "0")


miles = Label(text="Miles", font=("Arial",12))
miles.grid(column=2, row=0)

is_equal = Label(text="is equal to", font=("Arial",12))
is_equal.grid(column=0, row=1)

output = Label(text="0 Km", font=("Arial",12))
output.grid(column=1, row=1)


calc_btn = Button(text="Calculate", command=convert_miles_to_km, font=("Arial",12))
calc_btn.grid(column=1, row=2)


window.mainloop()
