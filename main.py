"""
For a summer reading program, we want to find out how many books students read during the summer.

There is a file at https://public.karat.io/content/test/test_file.txt with lines like this:

157,Kelly,a wrinkle in time,50
231,Selina,to kill a mockingbird,300
74,Juan,to kill a mockingbird,300
558,Elysse,hush hush,200

Each line contains four fields
* A unique ID for the reader
* The given name of a reader
* The name of a book.
* The number of pages in the book.

Fields will only contain letters, numbers, and spaces.

We would like to know how many books and how many pages were read this summer. Write a script that fetches/downloads the file, reads it, and outputs the total number of books read and total number of pages that were read. For example, for the four lines above, you would output 4 and 850.

Test output: (in any format, as long as the numbers are output)
Book count:  20015
Page count:  2805094
"""
import requests
import csv
from contextlib import closing

def get_book_details(url: str) -> (int, int):
    book_cnt = 0
    page_cnt = 0

    # 1. read file into memory
    with closing(requests.get(url, stream=True)) as r:
        lines = [line.decode('utf-8') for line in r.iter_lines()]
        reader = csv.reader(lines, delimiter=",")
        # 2. loop through each line in fileAddress (init counters for pages and number of books)
        for row in reader:
            # print(row)
            book_cnt += 1
            curr_pc = row[3]
            page_cnt += int(curr_pc)

    # 3 create result to return
    print(f"book count: {book_cnt}, page count: {page_cnt}")
    return book_cnt, page_cnt

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(get_book_details("https://conorheffron.github.io/student-books-test-data/students/books/data.txt"))
    # book count: 20015, page count: 2805094
    # (20015, 2805094)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
