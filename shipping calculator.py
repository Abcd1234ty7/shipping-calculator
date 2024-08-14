from tkinter import *
# import the tkinter libary to create GUI
# Create a function that will calculate when button is clicked


def on_calculate_button_click():
    # Get the input values
    total_cost = float(total_cost_entry.get())
    country_code = country_code_entry.get()

    # Calculate the shipping cost
    shipping_cost = calculate_shipping_cost(total_cost, country_code)

    # Update the label with the shipping cost
    shipping_cost_label.config(text='Shipping Cost: {}'.format(shipping_cost))

# function used to calculate shipping costs with the aid of conditional statements


def calculate_shipping_cost(total_cost, country_code):
    # Look up the shipping cost based on the country and total cost
    if country_code == 'SA':
        if total_cost < 5000:
            shipping_cost = 0
        elif total_cost < 9900:
            shipping_cost = 100
        elif total_cost < 24900:
            shipping_cost = 250
        else:
            shipping_cost = 500
    elif country_code == 'DC':
        if total_cost < 5000:
            shipping_cost = 100
        elif total_cost < 9900:
            shipping_cost = 200
        elif total_cost < 25000:
            shipping_cost = 500
        else:
            shipping_cost = 1000
    elif country_code == 'KY':
        if total_cost < 5000:
            shipping_cost = 50
        elif total_cost < 9900:
            shipping_cost = 150
        elif total_cost < 24900:
            shipping_cost = 300
        else:
            shipping_cost = 750
    elif country_code == 'NI':
        if total_cost < 5000:
            shipping_cost = 200
        elif total_cost < 9900:
            shipping_cost = 250
        elif total_cost < 24900:
            shipping_cost = 550
        else:
            shipping_cost = 1100
    else:
        shipping_cost = 'N/A'

    return shipping_cost
# Creates the GUI interface


GUI = Tk()
GUI.title('Shipping Cost Estimation Table')
GUI.configure(bg='yellow')  # Set the background color to red
# Create input fields
total_cost_label = Label(GUI, text='please enter the total Cost:')
total_cost_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
total_cost_entry = Entry(GUI)
total_cost_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

country_code_label = Label(GUI, text='Country Code[SA/DC/KY/NI]:')
country_code_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
country_code_entry = Entry(GUI)
country_code_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

# Create a button to calculate shipping cost
calculate_button = Button(GUI, text='Display shipping Cost', command=on_calculate_button_click)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create a label to display the result
shipping_cost_label = Label(GUI, text='Shipping Cost:')
shipping_cost_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)

# Start the event loop
GUI.mainloop()
# End of code

