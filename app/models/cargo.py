class Cargo:
    def __init__(self, item_id: str, name: str, width: float, depth: float, height: float, mass: float, priority: int, expiry_date: str, usage_limit: int, preferred_zone: str):
        self.item_id = item_id
        self.name = name
        self.width = width
        self.depth = depth
        self.height = height
        self.mass = mass
        self.priority = priority
        self.expiry_date = expiry_date
        self.usage_limit = usage_limit
        self.preferred_zone = preferred_zone