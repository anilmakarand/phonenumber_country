import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
inp_number=input("Enter phone number: ")
print("Number:"+inp_number)
number = phonenumbers.parse(inp_number)
print("Country:"+geocoder.country_name_for_number(number,'en'))
print("Carrier:"+carrier.name_for_number(number,'en'))
