# Task 1: Duplicate Entries Cleanup

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

unique_customer_ids = set(customer_ids)

print("Unique customer IDs:")

for customer_id in sorted(unique_customer_ids):
    print(customer_id)