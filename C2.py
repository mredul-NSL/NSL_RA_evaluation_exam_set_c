class Info: 
    def __init__(self, first_name, last_name, address, age): 
         self.first_name = first_name 
         self.last_name = last_name 
         self.address = address 
         self.age = age 
    
    def __repr__(self):
            return '({}, {}, {}, {})'.format(self.first_name, self.last_name, self.address, self.age)
  
infos = [ 
     Info("Mehadi", "Hasan", "Bogra", 28), 
     Info("Mehadi", "Hasan", "Bogra", 25), 
     Info("Kousar", "Rahman", "Dhaka", 30) 
]

sorted_infos = sorted(infos, key = lambda i: (i.first_name, i.last_name, i.address, i.age))


print("Object sorted: ", sorted_infos)