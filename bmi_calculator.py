import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("250x150")
root.resizable(0, 0)
root.configure(bg='lightblue')

# Add labels for weight and height
tk.Label(root, text="Weight (kg):", bg='lightblue').grid(row=0, column=0, padx=10, pady=(10, 5), sticky='e')
tk.Label(root, text="Height (m):", bg='lightblue').grid(row=1, column=0, padx=10, pady=(5, 10), sticky='e')

# Add entry widgets for weight and height
weight_entry = tk.Entry(root)
height_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=(10, 5))
height_entry.grid(row=1, column=1, padx=10, pady=(5, 10))

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        bmi_result.set(f"BMI: {bmi:.2f} ({category})")
    except ValueError:
        bmi_result.set("Please enter valid numbers")

# Function to reset the entries and result
def reset():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    bmi_result.set("")

# Add buttons for calculate and reset
button_frame = tk.Frame(root, bg='lightblue')
button_frame.grid(row=2, column=0, columnspan=2, pady=10)

calculate_button = tk.Button(button_frame, text="Calculate", command=calculate_bmi, width=10)
calculate_button.grid(row=0, column=0, padx=5)

reset_button = tk.Button(button_frame, text="Reset", command=reset, width=10)
reset_button.grid(row=0, column=1, padx=5)

# Add a label to display the BMI result
bmi_result = tk.StringVar()
tk.Label(root, textvariable=bmi_result, bg='lightblue').grid(row=3, column=0, columnspan=2, pady=5)

# Start the main loop
root.mainloop()

