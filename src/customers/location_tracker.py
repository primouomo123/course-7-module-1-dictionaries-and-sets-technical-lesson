# This module should implement unique location tracking using Set Operations
def get_unique_locations(self):
        """Placeholder for retrieving unique locations (students will implement)."""
        customer_locations = {customer["location"] for customer in self.customers.values()}
        print("\nUnique Customer Locations:", customer_locations)