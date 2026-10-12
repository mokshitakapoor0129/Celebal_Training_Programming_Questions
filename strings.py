order_id = "ORD-12345"
supplier = "Tech Supplies Inc."
description = "Order for 50 units of gaming laptops"

print(order_id)
print(type(order_id))
print(len(order_id))

tracking_number = "TRK-987654321"
print(tracking_number)
print(tracking_number[-1])
print(tracking_number[3:7])

status = "Shipped"

status = "s" + status[1:]
print(status)

status = "in transit"
clean_status = status.strip()
print(clean_status)

supplier = "Tech Supplies Inc."
clean_supplier = supplier.lower()
print(clean_supplier)

supplier = "TECH Supplies Inc."
clean_supplier = supplier.strip().title()
print(clean_supplier)

message = "Shipping delayed due to high demand."

if "delayed" in message.lower():
    print("Alert: Shipping delay detected.")
else:
    print("Shipping on schedule.")

    order_id = ODR12345

    if order_id.startswith("ORD"):
        print("Valid order ID.")
    else:
        print("Invalid order ID.")

        supplier_code = "TSI-001, Tech Supplies Inc., Bengluru"
        #details = supplier_code.split(", ")
        #print("Supplier Code:", details[0])
        #print("Supplier Name:", details[1])
        #print("Supplier Location:", details[2])
        status = "Active"
        location = "Chennai"

        message = f"Supplier Code: {supplier_code}, Status: {status}, Location: {location}"
        print(message)

        products = ("laptop", "smartphone", "tablet", "headphones", "Smartwatch")
        summary = ", ".join(products)
        print("Available product: (summary)")

        order_id = "ORD-12345"
        amount = 15000

        print(f"Order ID: {order_id} confirmed. Total amount: ${amount:.2f}.")
        







