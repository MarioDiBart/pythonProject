# This is a sample Python script.
from CSVModifer import *
from Tests import *


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

file = '/Users/mariodibartolomeo/Library/Containers/com.microsoft.Excel/Data/Desktop/revTester.xlsx'
filetwo = '/Users/mariodibartolomeo/Library/Containers/com.microsoft.Excel/Data/Desktop/empty.xlsx'
file1 = CSVModifer()
file2 = CSVModifer()

'''def run_tests():
    return MyTestCase().test_something()
'''

# Use a breakpoint in the code line below to debug your script.

def printFile():
    file1.set_file(file)
    file2.set_file(filetwo)
    file1.set_workbook(file)
    file2.set_workbook(filetwo)
    file1.set_worksheet("2022 Unearned Revenue")
    file2.set_worksheet("Sheet1")
    file2.worksheet = file1.worksheet
    file2.get_sheetnames()
    #file2.load()
    file2.workbook.save(filetwo)

    # Press the green button in the gutter to run the script.


if __name__ == '__main__':
    # run_tests()
    printFile()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
