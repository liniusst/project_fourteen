from typing import List
import logging
logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
# Write a function that moves all elements of one type to the end of the list:
# move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]

def move_to_end(input_list: List[int], input_number: int) -> List[int]:
    try: 
        if input_number in input_list:
            count = input_list.count(input_number)
            logging.info(f"Here are {count} elements with same value and while function starting his job")
            while count != 0:
                input_list.remove(input_number)
                input_list.append(input_number)
                count -= 1
            logging.info("While end his job")
        return input_list
    except Exception as error_code:
        logging.error(f"Error: {error_code}")

if __name__ == "__main__":
    print(move_to_end(input_list= [1, 3, 2, 4, 4, 1], input_number= 2))
