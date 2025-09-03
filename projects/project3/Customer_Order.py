from datastructures.linkedlist import LinkedList
from projects.project3.Drink import Drink
from projects.project3.Menu import Menu
class Customer_Order:
    def __init__(self, name):
        self._order = LinkedList(data_type= Drink)
        self.name = name
        self._count = 0

    def add_drink(self, drink) -> None:
        customize = input("Do you want customization? (Y)es or (N)o:")
        if customize == 'Y':
            customization_description = input("please take customization request")
            drink.customization == customization_description
        self._order.append(drink)

    def remove_drink(self, drink) ->None:
        self._order.remove(drink)

    def restart_order(self,drink) -> None:
        self._order.clear()
    
    def repeat_order(self) -> None:
        for order in self._order:
            print(order)
    
    def total(self) -> float:
        sum = 0
        for order in self._order:
            sum += order.price
        return sum
    def total_sold(self) -> int:
        return self._count
    
    def take_order(self) -> Drink:
        menu_obj = Menu()
        menu = menu_obj.return_items()
        menu_obj.print_menu()
        more = 'Y'
        while  more.upper() == 'Y':
            start = int(input('What drink would you like today? (Enter number): '))
            if start == 1:
                self.add_drink(menu[0])
            elif start == 2:
                self.add_drink(menu[1])
            elif start == 3:
                self.add_drink(menu[2])
            elif start == 4:
                self.add_drink(menu[3])
            elif start == 5:
                self.add_drink(menu[4])
            more = input('Would you like to order another? (Y)es or (N)o: ')

        self._count += 1
        return self
        
    def __repr__(self):
        drinks = ", ".join(str(drink) for drink in self in self._order)
        return f"Order for {self.name}: [{drinks}] with {len(self._order)} drink(s)."
                




