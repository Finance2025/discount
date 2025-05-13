# Parent class
class Device:
    def _init_(self, brand, model):
        self.brand = brand
        self.model = model

    def get_info(self):
        return f"Device: {self.brand} {self.model}"

# Child class (inherits from Device)
class Smartphone(Device):
    def _init_(self, brand, model, storage, battery):
        super()._init_(brand, model)
        self.__storage = storage  # private attribute (encapsulation)
        self.battery = battery

    def get_storage(self):
        return f"Storage: {self.__storage}GB"

    def charge(self):
        return f"{self.brand} {self.model} is charging..."

# Create an object
phone = Smartphone("Samsung", "Galaxy A50", 128, "4000mAh")
print(phone.get_info())
print(phone.get_storage())
print(phone.charge())