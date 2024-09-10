from time import time
from numpy import number
import phonenumbers
from phonenumbers import timezone,geocoder,carrier

number= input("Enter your Phone Number:")
phone= phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")

print(phone)
print(time)
print(car)
print(reg)
