from django.contrib.auth.models import User
from django.db import models
import random

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class State(models.Model):
    name = models.CharField(max_length=100)
    code = models.PositiveIntegerField(unique=True)  # This will represent the numerical distance value

    def __str__(self):
        return self.name
    
    @staticmethod
    def calculate_distance(state1_code, state2_code):
        try:
            state1 = State.objects.get(code=state1_code)
            state2 = State.objects.get(code=state2_code)
            return abs(state1.code - state2.code)  # Simple absolute difference
        except State.DoesNotExist:
            return None
        

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user who placed the order
    origin = models.ForeignKey(State, related_name='origin_state', on_delete=models.CASCADE)  # Origin state
    destination = models.ForeignKey(State, related_name='destination_state', on_delete=models.CASCADE)  # Destination state
    fluid_quantity = models.FloatField()  # The quantity of petroleum fluid (in liters or another unit)
    distance = models.IntegerField()  # Distance between origin and destination
    price = models.FloatField()  # Final calculated price

    def save(self, *args, **kwargs):
        # Calculate the distance between origin and destination
        self.distance = abs(self.origin.code - self.destination.code)
        
        # Calculate price: for simplicity, let's assume price is based on distance and fluid quantity
        base_price_per_unit = 10  # Base price per unit (you can adjust this)
        distance_price_factor = 0.5  # Price increases based on distance
        fluid_price_factor = 2  # Price increases based on fluid quantity

        # Calculate price with some randomness (to simulate fluctuations)
        price = (self.distance * distance_price_factor + self.fluid_quantity * fluid_price_factor) * random.uniform(0.9, 1.2)
        self.price = round(price, 2)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.id} from {self.origin.name} to {self.destination.name}"
