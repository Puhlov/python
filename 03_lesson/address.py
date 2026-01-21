class Address:
    def __init__(self, indeks, street, city, house, apartment):
        self.indeks = indeks
        self.street = street
        self.city = city
        self.house = house
        self.apartment = apartment

    def __str__(self):
        return f"{self.indeks}, {self.city}, {self.street}, {self.house}, {self.apartment}"