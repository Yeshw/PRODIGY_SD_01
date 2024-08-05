import tkinter as tk
from tkinter import ttk

class TemperatureConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")

        self.create_widgets()

    def create_widgets(self):
        self.temperature_label = ttk.Label(self.root, text="Enter temperature:")
        self.temperature_label.grid(row=0, column=0, padx=10, pady=10)

        self.temperature_entry = ttk.Entry(self.root, width=20)
        self.temperature_entry.grid(row=0, column=1, padx=10, pady=10)

        self.unit_label = ttk.Label(self.root, text="Select unit:")
        self.unit_label.grid(row=1, column=0, padx=10, pady=10)

        self.unit_combobox = ttk.Combobox(self.root, values=["Celsius", "Fahrenheit", "Kelvin"])
        self.unit_combobox.current(0)  # Set default selection to Celsius
        self.unit_combobox.grid(row=1, column=1, padx=10, pady=10)

        self.convert_button = ttk.Button(self.root, text="Convert", command=self.convert_temperature)
        self.convert_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.result_label_celsius = ttk.Label(self.root, text="")
        self.result_label_celsius.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.result_label_fahrenheit = ttk.Label(self.root, text="")
        self.result_label_fahrenheit.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        self.result_label_kelvin = ttk.Label(self.root, text="")
        self.result_label_kelvin.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    def convert_temperature(self):
        try:
            temperature = float(self.temperature_entry.get())
            original_unit = self.unit_combobox.get()

            if original_unit == "Celsius":
                celsius = temperature
                fahrenheit = celsius * 9/5 + 32
                kelvin = celsius + 273.15
            elif original_unit == "Fahrenheit":
                fahrenheit = temperature
                celsius = (fahrenheit - 32) * 5/9
                kelvin = (fahrenheit - 32) * 5/9 + 273.15
            elif original_unit == "Kelvin":
                kelvin = temperature
                celsius = kelvin - 273.15
                fahrenheit = celsius * 9/5 + 32
            else:
                raise ValueError("Invalid unit selected")

            self.result_label_celsius.config(text=f"{temperature:.2f} {original_unit} = {celsius:.2f} Celsius")
            self.result_label_fahrenheit.config(text=f"{temperature:.2f} {original_unit} = {fahrenheit:.2f} Fahrenheit")
            self.result_label_kelvin.config(text=f"{temperature:.2f} {original_unit} = {kelvin:.2f} Kelvin")

        except ValueError:
            self.result_label_celsius.config(text="Invalid input. Please enter a valid number.")
            self.result_label_fahrenheit.config(text="")
            self.result_label_kelvin.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverter(root)
    root.mainloop()



