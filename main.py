# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from application.salary import calculate_salary
from application.db.people import get_employees

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_employees()
    calculate_salary()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
