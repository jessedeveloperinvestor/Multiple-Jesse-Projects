#pip install Faker
from faker import Faker
fake=Faker('pt_br')
print(fake.name(), '\n')
print(fake.address(), '\n')
print(fake.email(), '\n')
print(fake.text(), '\n')
print(fake.phone_number(), '\n')