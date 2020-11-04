from people import get_employees
from salary import calculate_salary
from datetime import datetime

def main():
    while True:
        print(datetime.today())
        command = input('Введите команду')
        if command == 's':
            calculate_salary(22)
        if command == 'w':
            get_employees(22)
if __name__ == '__main__':
    main()