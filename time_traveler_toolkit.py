import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module
from custom_module import generate_time_travel_message

current_datetime = dt.datetime.now()

formatted_datetime = current_datetime.strftime("%d/%m/%Y %H:%M:%S")

print(f"Current date and time: {formatted_datetime}")

current_year = dt.datetime.now().year

target_year = randint(1500, 3000)

base_cost = Decimal('199.99')

year_difference = abs(target_year - current_year)

cost_multiplier = Decimal('1.75')

destinations = ["Neo Tokyo", "Ancient Rome", "Cyber Cairo", "Atlantis Reborn", "New Paris"]
destination = choice(destinations)

final_cost = base_cost + (cost_multiplier * year_difference)

final_cost = final_cost.quantize(Decimal('0.01'))


message = generate_time_travel_message(target_year, destination, final_cost)
print(message)