"""
For a summer reading program, we want to find out how many books students read during the summer.

There is a file at  https://conorheffron.github.io/student-books-test-data/students/books/data.txt
with lines like this:

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

We would like to know how many books and how many pages were read this summer.
Write a script that fetches/downloads the file, reads it,
and outputs the total number of books read and total number of pages that were read.

For example, for the four lines above, you would output 4 and 850.

Test output: (in any format, as long as the numbers are output)
Book count:  20015
Page count:  2805094
"""
import argparse
from contextlib import closing
import csv
from io import StringIO
import pandas as pd
import requests

def get_book_details_requests_csv(file_address: str) -> (int, int):
    book_cnt = 0
    page_cnt = 0

    # read file into memory
    with closing(requests.get(file_address, stream=True)) as reader:
        lines = [line.decode('utf-8') for line in reader.iter_lines()]
        rows = csv.reader(lines, delimiter=",")
        # loop through each line in fileAddress (init/inc counters for pages & number of books)
        for row in rows:
            # print(row)
            book_cnt += 1
            curr_pc = row[3]
            page_cnt += int(curr_pc)

    # create result to return
    # print(f"book count: {book_cnt}, page count: {page_cnt}")
    return book_cnt, page_cnt

def get_book_details_pandas(file_address: str) -> (int, int):
    # Fetch the content using requests
    response = requests.get(file_address)
    response.raise_for_status()  # Ensure the request was successful

    # Read the CSV content into a DataFrame
    df_books_prog = pd.read_csv(StringIO(response.text),
                     header=None,
                     names=['id', 'read_name', 'book_name', 'pages_read'])
    book_cnt = df_books_prog.count()
    page_cnt = df_books_prog.pages_read.sum()

    return int(book_cnt.iloc[0]), int(page_cnt)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="A simple script to check student ready progress.")
    parser.add_argument("--fileAddr",
                        type=str,
                        required=True,
                        help="HTTP Address for File Content for analysis")
    # Parse the arguments
    args = parser.parse_args()

    # Expected -> book count: 20015, page count: 2805094
    # (20015, 2805094)
    url = args.fileAddr
    print(f"Result of get_book_details_requests_csv={get_book_details_requests_csv(url)}")
    print(f"Result of get_book_details_pandas={get_book_details_pandas(url)}")
