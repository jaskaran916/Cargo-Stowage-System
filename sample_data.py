import csv

def load_items(filename):
    items = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            items.append(row)
    return items

def load_containers(filename):
    containers = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            containers.append(row)
    return containers 
