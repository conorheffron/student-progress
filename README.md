# student-progress

[![Pip & Pytest CI](https://github.com/conorheffron/student-progress/actions/workflows/python-app.yml/badge.svg)](https://github.com/conorheffron/student-progress/actions/workflows/python-app.yml)

[![Pylint](https://github.com/conorheffron/student-progress/actions/workflows/pylint.yml/badge.svg)](https://github.com/conorheffron/student-progress/actions/workflows/pylint.yml)

## Tech
 - Python 3, venv, pandas, requests

### Command Line Usage
 - Success
```shell
(.venv) student-progress % python3 main.py --fileAddr="https://conorheffron.github.io/student-books-test-data/students/books/data.txt"
Result of get_book_details_requests_csv=(20015, 2805094)
Result of get_book_details_pandas=(20015, 2805094)
```
 - Fail
```shell
(.venv) student-progress % python3 main.py 
usage: main.py [-h] --fileAddr FILEADDR
main.py: error: the following arguments are required: --fileAddr
```
