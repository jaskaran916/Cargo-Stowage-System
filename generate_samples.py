 import csv
import random

def generate_samples(num_samples):
    items = []
    for i in range(num_samples):
        item_id = f"{i:03}"
        name = f"Item {item_id}"
        width = random.randint(5, 30)
        depth = random.randint(5, 30)
        height = random.randint(5, 30)
        mass = random.uniform(1, 10)
        priority = random.randint(1, 100)
        expiry_date = "2025-12-31"
        usage_limit = random.randint(1, 100)
        preferred_zone = random.choice(["Crew Quarters", "Airlock", "Laboratory"])
        items.append([item_id, name, width, depth, height, mass, priority, expiry_date, usage_limit, preferred_zone])
    
    with open('input_items.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Item ID", "Name", "Width", "Depth", "Height", "Mass", "Priority", "Expiry Date", "Usage Limit", "Preferred Zone"])
        writer.writerows(items)

if __name__ == "__main__":
    generate_samples(100)
