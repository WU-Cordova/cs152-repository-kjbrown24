#Drink Ordering System

This project is a simple command line program where customers can order drinks, review their order, and confirm it. The system also trakcs open and completed orders and shows a report at the end of the day.

1. Menu
#Data Stucture: Python List
#The menu uses a list to store drink objects. This makes it easy to loop through and display each drink.
#Getting a drink by its number is fast 0(1) time.

2. Customer Order
#Data Structure: Linked List
#A linked list lets us add or remove drinks easily as the customer builds their order.
#Adding a drink is fast 0(1). Removing ot printing the order takes 0(n).

3. Order Confirmation
#Data Stucture: Uses methods in the Customer_Order class
#After an order is created, it's printed out using a loop. No extra data structure is needed.
#Printing the order takes 0(n), where where n is the number of drinks.

4. Open Orders Queue
#Data Strucure: Deque
#Orders are handled in the order they were places (FIFO). A deque supports fast adding/ removing from both ends.
#Adding and removing order is 0(1) time.

5. Completed Orders
#Data Strucutre: Stack
#Completed order are stored in a stack so we can later pop them out and check them for the report.
#pushing and popping are both 0(1) time.

1. Make sure you have all files and folders:
`program.py` `Menu.py`, `Drink.py` `Customer_Order.py`, `Order_Queue.py`
   `datastructures` folder with `array`, `linkedlist`, `deque`, and `liststack`

click run in terminal to program.py

Drink Ordering System
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Next Order as Complete
5. End-of-Day Report
6. Exit
Choose an option (1-6): 2
Customer name: Alex

Available Drinks:
1. Drink(name='Hot Cocoa', price=4.0, size='Medium', customization=' ')
2. Drink(name='Americano', price=4.25, size='Medium', customization=' ')
...

Would you like to order another? (Y)es or (N)o: N
Confirm this order? (Y/N): Y

Open Orders:
- Alex:
Drink(name='Latte', price=5.0, size='Medium', customization='extra foam')

End-of-Day Report:
Latte: 1 sold, $5.00
Total Revenue: $5.00

#Things I would do if I have more time
Fix the bug with customization not saving.
Add input checks so users can’t crash the program.
Save orders to a file and load them again later.
Add more drink options and sizes.





