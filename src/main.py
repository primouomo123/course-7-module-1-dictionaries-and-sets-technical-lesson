from customers.customer_manager import CustomerManager, update_customer_location
from customers.filters import filter_customers_by_city
from customers.location_tracker import get_unique_locations

# Initial dictionary of customers (students will enhance this later)
customers = {
    "cust_101": {"name": "Alice", "location": "New York", "purchases": ["Laptop", "Mouse"]},
    "cust_102": {"name": "Bob", "location": "Los Angeles", "purchases": ["Phone", "Charger"]},
    "cust_103": {"name": "Charlie", "location": "New York", "purchases": ["Tablet", "Headphones"]}
}

customer_manager = CustomerManager(customers)

print("\nAll Customers:")
customer_manager.display_customers()

# Filtering is not yet implemented (students will add it)
filter_customers_by_city(customer_manager, "New York")

# Unique locations are not yet implemented (students will add them)
get_unique_locations(customer_manager)

update_customer_location(customer_manager, "cust_102", "San Francisco")

get_unique_locations(customer_manager)
