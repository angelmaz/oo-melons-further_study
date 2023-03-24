"""Classes for melon orders."""
import random
import datetime


class TooManyMelonsError(ValueError):
    def __init__(self):
        super().__init__("Too many melons!")
    
class AbstractMelonOrder:
    
    def __init__(self, species, qty,):
        #you don't need to pass shipped in the parameter because "shipped" will always start out as False
        self.species = species
        if qty > 100:
            raise TooManyMelonsError
        
        self.qty = qty


        self.shipped = False 

    def mark_shipped(self):
        """checks order has been shipped"""
        self.shipped = True

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == "Christams melon":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total
    
    def get_base_price(self):
        base_price = random.randrange(5,10)
   
        now = datetime.datetime.now()
        if now.hour >= 8 and now.hour <= 11 and now.weekday() < 5:
            base_price += 4

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08
    


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17
    
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code
     
    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmaentMelonOrder(AbstractMelonOrder):
    
    order_type = "government"
    tax = 0.0

    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed
