from main import get_book_details_requests_csv, get_book_details_pandas


def test_pandas_approach():
    result = get_book_details_pandas(
        "https://conorheffron.github.io/student-books-test-data/students/books/data.txt")

    assert result == (20015, 2805094)

def test_raw_csv_requests_approach():
    result = get_book_details_requests_csv(
        "https://conorheffron.github.io/student-books-test-data/students/books/data.txt")

    assert result == (20015, 2805094)

def test_pandas_sm_approach():
    result = get_book_details_pandas(
        "https://conorheffron.github.io/student-books-test-data/students/books/test_sm_data.txt")

    assert result == (4, 800)

def test_raw_csv_sm_requests_approach():
    result = get_book_details_requests_csv(
        "https://conorheffron.github.io/student-books-test-data/students/books/test_sm_data.txt")

    assert result == (4, 800)
