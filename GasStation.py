class Fuel:
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount

    def get_amount(self):
        return fuel_amount * self.price * self.discount


fuel1 = Fuel('Diesel', 300.05, 0.2)
fuel2 = Fuel('Super', 297.05, 0.1)
fuel3 = Fuel('Petrol', 299.98, 0.3)
fuel4 = Fuel('V_Power', 302.05, 0.2)


print('1.Diesel \n2.Super \n3.Petrol \n4.V-Power')
fuel_type = int(input('\nEnter the number representing the fuel type : '))

fuel_amount = int(input(f'\nEnter the fuel amount in litres:'))

if fuel_type == 1:
    print(f'\nYou picked Diesel of {fuel_amount} litres.')
    print(f'\nTotal amount payable is: {Fuel.get_amount(fuel1)}')

if fuel_type == 2:
    print(f'\nYou picked Super of {fuel_amount} litres.')
    print(f'\nTotal amount payable is: {Fuel.get_amount(fuel2)}')

if fuel_type == 3:
    print(f'\nYou picked Petrol of {fuel_amount} litres.')
    print(f'\nTotal amount payable is: {Fuel.get_amount(fuel3)}')

if fuel_type == 4:
    print(f'\nYou picked V-Power of {fuel_amount} litres.')
    print(f'Total amount payable is: {Fuel.get_amount(fuel4)}')
