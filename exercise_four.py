from typing import List, Dict
import logging
logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

# Create a program that takes 4 data types/structures: strings, numbers, list, dict. 
# Iterate 10 times with inputs and log what data type/structure and how many times was entered. 
# Handle all possible errors and log it.

users_database = ['Linas', 'Antanas']
pin_codes_db = [9999, 1234]
users_permissions = {'Linas': 'admin', 'Antanas': 'member'}

def mix_all_data(name: str, pin_code: int, user_db: List[str], permission: Dict[str, str]) -> None:
    try:
        logging.info(f'Someone trying log in with {name_input} name and {pin_input} pin')
        if name_input in user_db:
            logging.warning(f'We found {name_input} in our DB and pass to input pin code')
            if pin_input in pin_codes_db:
                logging.info(f'User logged successfully! User: {name_input} have {permission[name_input]} rights')
            else:
                logging.warning(f'Bad pin code. User try log in with {pin_input} pin')
        else:
            logging.warning(f'User with {name_input} not found! and we end here')
    except ValueError:
        logging.error('ValueError: Given just one value, need name and pin')

if __name__ == "__main__":
    name_input, pin_input = input('Enter admin name and pin code: ').split()
    pin_input = int(pin_input)
    mix_all_data(name = name_input, pin_code= pin_input, user_db= users_database, permission= users_permissions)
