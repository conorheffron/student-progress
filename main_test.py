from main import get_book_details_requests_csv, get_book_details_pandas


def test_pandas_approach_large_file():
    result = get_book_details_pandas(
        "https://conorheffron.github.io/student-books-test-data/students/books/data.txt")

    assert result == (20015, 2805094)

def test_raw_csv_requests_approach_large_file():
    result = get_book_details_requests_csv(
        "https://conorheffron.github.io/student-books-test-data/students/books/data.txt")

    assert result == (20015, 2805094)

def test_pandas_approach_small_file():
    result = get_book_details_pandas(
        "https://conorheffron.github.io/student-books-test-data/students/books/test_sm_data.txt")

    assert result == (4, 850)

def test_raw_csv_requests_small_file():
    result = get_book_details_requests_csv(
        "https://conorheffron.github.io/student-books-test-data/students/books/test_sm_data.txt")

    assert result == (4, 850)
