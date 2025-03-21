from inventory_management import *

def unit_test():
    """Test individual functions in isolation."""
    
    add_product('apple', 50)  
    add_product('banana', 20)  

    result = sell_product('apple', 10)
    result = sell_product('banana', 200) 
 
def integration_test():
    """Test how different functions from the Inventory Management module work together."""
  
    add_product('apple', 50)
    add_product('banana', 30)

    sell_product('apple', 10)
    sell_product('banana', 5)

    apple_stock = check_availability('apple')
    banana_stock = check_availability('banana')

    print("\n----- Integration Test Results -----")
    print(f"Apple stock after sale: {apple_stock} (Expected: 40)")  
    print(f"Banana stock after sale: {banana_stock} (Expected: 25)")  
    print(f"Total inventory value: {total_inventory_value()} (Expected: 70)")

def system_test():
    """Test the system as a whole."""
    
    add_product('apple', 50)
    add_product('banana', 30)
    sell_product('apple', 10)
    sell_product('banana', 5)

    apple_stock = check_availability('apple')
    banana_stock = check_availability('banana')
    inventory_value = total_inventory_value()

    print("\n----- System Test Results -----")
    print(f"Apple stock: {apple_stock} (Expected: 40)")  
    print(f"Banana stock: {banana_stock} (Expected: 25)")  
    print(f"Total inventory value: {inventory_value} (Expected: 70)") 
    
if __name__ == "__main__":
    print("Running Unit Test...")
    unit_test()
    print("Running Integration Test...")
    integration_test()
    print("Running System Test...")
    system_test 