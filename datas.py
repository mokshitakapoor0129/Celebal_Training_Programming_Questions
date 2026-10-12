products = ("laptop", "smartphone", "tablet", "headphones")

products.append("monitor")
products[0] = "gaming laptop"
products.remove("tablet")

print(products)

print("Watch" in products)

product = ("P1", "keyboard", 3500)
product_id, name, price = product

#Dictionaries
inventory = {
    "P1": {"name": "keyboard", "price": 3500, "quantity":50},
    "P2": {"name": "mouse", "price": 1500, "quantity": 100},
    "P3": {"name": "monitor", "price": 12000, "quantity": 30}
}
print(inventory)
print(inventory.keys())
print(inventory.values())

    #sets
online_customers = {"Alice", "Bob", "Charlie", "David"}
returning_customers = {"bob", "Eve", "Frank", "Grace"}

#function of two sets
print(online_customers | returning_customers)
#intersection of two sets
print(online_customers & returning_customers)
#differance of two sets
print(online_customers - returning_customers)

