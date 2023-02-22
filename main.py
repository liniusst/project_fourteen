# keturiolikta pamokas
import logging
# logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')



# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

def check_amount(amount: float) -> None:
    logging.info(f'asdasd asd')

def add_few_number(a: int, b: int) -> int:
    logging.debug(f'Received numbers: a {a} and b:{b}')
    return a + b

add_few_number(a=6, b=7)


def emergency_stop(is_stop_event: bool) -> None:
    if is_stop_event:
        logging.critical(f'Had to stop device due to unexpected stop event')

emergency_stop(True)
