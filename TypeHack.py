
from colorama import Fore # pip3 install colorama
from faker import Faker #pip3 install faker
import time

faker = Faker()

for _ in range(200):
  print(Fore.GREEN, faker.pydict())
  time.sleep(0.01)
print("[HACKER VOICE] I'm In")
print("YOU HAVE GAINED ROOT ACCESS")
