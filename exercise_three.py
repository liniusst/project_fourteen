import logging
from random import randint
logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

# Create 3 functions, that are related to each other (one is being called in another), and test all logger severity levels by your own design.


fuel_level = randint(0, 10)
actual_level = randint(0, 10)


def check_fuel_level(level: int) -> bool:
    return level >= fuel_level

def start_engine(name: int):
    if check_fuel_level == True:
        print('true')
    else:
        print("false")


# print(check_fuel_level(actual_level))
start_engine(2)

