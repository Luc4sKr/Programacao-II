# biblioteca capaz de gerar dados falsos
from faker import Faker

fake = Faker()

nome = fake.name()
user = fake.user_name()
senha = fake.password()
mes = fake.month()

print(nome)
print(user)
print(senha)
print(mes)
