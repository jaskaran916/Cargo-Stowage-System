 import csv

def generate_containers():
    containers = [
        ["contA", "Crew Quarters", 100, 85, 200],
        ["contB", "Airlock", 50, 85, 200],
        ["contC", "Laboratory", 200, 85, 200],
    ]
    
    with open('containers.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Container ID", "Zone", "Width", "Depth", "Height"])
        writer.writerows(containers)

if __name__ == "__main__":
    generate_containers()
