class Agent:

    def __init__(self, Agent_Breed, Policy_ID, Age, Social_Grade, Payment_at_Purchase, Attribute_Brand, Attribute_Price, Attribute_Promotions, Auto_Renew, Inertia_for_Switch):
        ### Convert string to float
        Age = float(Age)
        Social_Grade = float(Social_Grade)
        Payment_at_Purchase = float(Payment_at_Purchase)
        Auto_Renew = float(Auto_Renew)
        Inertia_for_Switch = float(Inertia_for_Switch)

        ### Initialization
        self.Agent_Breed = Agent_Breed
        self.Breed_Status = ''
        self.changetimes = 0
        self.Policy_ID = str(Policy_ID)
        self.Age = int(Age)
        self.Social_Grade = int(Social_Grade)
        self.Payment_at_Purchase = int(Payment_at_Purchase)
        self.Attribute_Brand = float(Attribute_Brand)
        self.Attribute_Price = float(Attribute_Price)
        self.Attribute_Promotions = float(Attribute_Promotions)
        self.Auto_Renew = int(Auto_Renew)
        self.Inertia_for_Switch = int(Inertia_for_Switch)
        self.Affinity = self.Payment_at_Purchase/self.Attribute_Price + (2 * self.Attribute_Promotions * self.Inertia_for_Switch)

