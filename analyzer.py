# --- THE DATASET ---
raw_transactions = [
    {"order_id": 101, "customer": "Alice", "item": "Laptop", "price": "$1200.00", "quantity": 1, "status": "completed"},
    {"order_id": 102, "customer": "Bob", "item": "Mouse", "price": "25.50", "quantity": 2, "status": "cancelled"},
    {"order_id": 103, "customer": "Charlie", "item": "Keyboard", "price": "45.00", "quantity": 1, "status": "completed"},
    {"order_id": 104, "customer": "Alice", "item": "Monitor", "price": "300.00", "quantity": 2, "status": "completed"},
    {"order_id": 105, "customer": "Diana", "item": "Desk", "price": "$150.00", "quantity": 1, "status": "pending"},
    {"order_id": 106, "customer": "Bob", "item": "Headphones", "price": "$80.00", "quantity": 1, "status": "completed"}
]


# --- PART 1: CLEAN THE PRICE ---
def clean_price(price_str):
    """Takes a price string (e.g., '$1200.00'), removes the '$', and returns it as a float."""
    return float(price_str.replace("$", ""))


# --- PART 2: FILTER ORDERS ---
def filter_completed_orders(transactions):
    """Takes the dataset and returns a new list containing only completed orders."""
    completed_list = []
    for order in transactions:
        if order["status"] == "completed":
            completed_list.append(order)
    return completed_list


# --- PART 3: CALCULATE REVENUE ---
def calculate_total_revenue(transactions):
    """Calculates total revenue (price * quantity) for all valid completed orders."""
    completed = filter_completed_orders(transactions)
    total_sum = 0
    
    for order in completed:
        price_float = clean_price(order["price"])
        total_sum += price_float * order["quantity"]
        
    return total_sum


# --- PART 4: FIND THE TOP CUSTOMER ---
def find_top_customer(transactions):
    """Determines which customer spent the most money overall on completed orders."""
    completed = filter_completed_orders(transactions)
    customer_totals = {}
    
    for order in completed:
        customer = order["customer"]
        price_float = clean_price(order["price"])
        item_total = price_float * order["quantity"]
        
        # Accumulate spending per customer
        if customer in customer_totals:
            customer_totals[customer] += item_total
        else:
            customer_totals[customer] = item_total
            
    # Find the customer with the maximum total spending
    top_customer = max(customer_totals, key=customer_totals.get)
    return top_customer, customer_totals[top_customer]


# --- RUNNING THE PIPELINE ---
if __name__ == "__main__":
    print("=== E-COMMERCE DATA ANALYSIS REPORT ===")
    
    revenue = calculate_total_revenue(raw_transactions)
    print(f"Total Revenue from Completed Orders: ${revenue:,.2f}")
    
    top_cust, top_spent = find_top_customer(raw_transactions)
    print(f"Top Spending Customer: {top_cust} (Total Spent: ${top_spent:,.2f})")
