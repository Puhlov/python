class Smartphone:
    def __init__(self, marka, model, number):
        self.marka = marka
        self.model = model
        self.number = number

    def get_marka(self):
        return self.marka

    def get_model(self):
        return self.model
    
    def get_number(self):
        return self.number

    def get_Smartphone_info(self):
        return f"Марка: {self.marka}, Модель: {self.model}, Номер телефона: {self.number}"