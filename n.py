def restock_alert(inventory, threshold):
    return [k for k,v in inventory.items() if int(v) < threshold]
inventory = {
        "apples": 5,
        "bananas": 2,
        "oranges": 10
    }
print(restock_alert(inventory,5))