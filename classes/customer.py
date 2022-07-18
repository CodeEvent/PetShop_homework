class Customer:
    def __init__(self, name, cash):
    
        self.name = name
        self.cash = cash
        self.total_pets = []

    def reduce_cash(self, customer_wallet):
        self.cash = customer_wallet
        
    def pet_count(self):
        return len(self.total_pets)
    
    def add_pet(self, pet):
        self.total_pets.append(pet)
        
    def get_total_value_of_pets(self):
        total = 0
        for pet in self.total_pets:
            total += pet.price
        return total
    
    
    