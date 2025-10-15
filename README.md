# student-progress

## Tech
Python 3, venv

### Usage
 - Success
```shell
(.venv) student-progress % python3 main.py --fileAddr="https://conorheffron.github.io/student-books-test-data/students/books/data.txt"
Hi, PyCharm
book count: 20015, page count: 2805094
(20015, 2805094)
```
 - Fail
```shell
(.venv) student-progress % python3 main.py                                                                                   
Hi, PyCharm
usage: main.py [-h] --fileAddr FILEADDR
main.py: error: the following arguments are required: --fileAddr
```