import phonenumbers
from phonenumbers import geocoder
Number='+'+input('Type in your phone number with country and state codes, like this: 5511912345678\n')
phone_number=phonenumbers.parse(Number)
print('This phone number is located in the state of '+geocoder.description_for_number(phone_number,'en'))