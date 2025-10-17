from main import create_report, tabulate_to_file, tabulate_to_console, sort_brands
from tabulate import tabulate


def test_create_report():
    assert create_report("rating", ["products1.csv", "products2.csv"]) == \
           {'apple': [4.550000000000001, 4], 'samsung': [4.533333333333333, 3], 'xiaomi': [4.366666666666666, 3]}
    assert create_report("rating", ["products1.csv"]) == \
           {'apple': [4.800000000000001, 2], 'xiaomi': [4.6, 1], 'samsung': [4.5, 2]}
    assert create_report("rating", ["products2.csv"]) == \
           {'samsung': [4.6, 1], 'apple': [4.3, 2], 'xiaomi': [4.25, 2]}


def test_tabulate_to_file():
    assert tabulate_to_file(
        {'apple': [4.550000000000001, 4], 'samsung': [4.533333333333333, 3], 'xiaomi': [4.366666666666666, 3]},
        "rating"
    ) == [['brand', 'rating'], ['apple', '4.55'], ['samsung', '4.53'], ['xiaomi', '4.37']]
    assert tabulate_to_file(
        {'apple': [4.800000000000001, 2], 'xiaomi': [4.6, 1], 'samsung': [4.5, 2]}, "rating"
    ) == [['brand', 'rating'], ['apple', '4.80'], ['xiaomi', '4.60'], ['samsung', '4.50']]
    assert tabulate_to_file(
        {'samsung': [4.6, 1], 'apple': [4.3, 2], 'xiaomi': [4.25, 2]}, "rating"
    ) == [['brand', 'rating'], ['samsung', '4.60'], ['apple', '4.30'], ['xiaomi', '4.25']]


def test_tabulate_to_console():
    assert tabulate_to_console(
        {'apple': [4.550000000000001, 4], 'samsung': [4.533333333333333, 3], 'xiaomi': [4.366666666666666, 3]},
        "rating"
    ) == tabulate([[1, 'apple', '4.55'], [2, 'samsung', '4.53'], [3, 'xiaomi', '4.37']],
                  headers=["", "brand", "rating"], tablefmt="pretty")
    assert tabulate_to_console(
        {'apple': [4.800000000000001, 2], 'xiaomi': [4.6, 1], 'samsung': [4.5, 2]}, "rating"
    ) == tabulate([[1, 'apple', '4.80'], [2, 'xiaomi', '4.60'], [3, 'samsung', '4.50']],
                  headers=["", "brand", "rating"], tablefmt="pretty")
    assert tabulate_to_console(
        {'samsung': [4.6, 1], 'apple': [4.3, 2], 'xiaomi': [4.25, 2]}, "rating"
    ) == tabulate([[1, 'samsung', '4.60'], [2, 'apple', '4.30'], [3, 'xiaomi', '4.25']],
                  headers=["", "brand", "rating"], tablefmt="pretty")


def test_sort_brands():
    assert sort_brands({'apple': [4.550000000000001, 4], 'samsung': [4.533333333333333, 3],
                        'xiaomi': [4.366666666666666, 3]}) ==\
           {'apple': [4.550000000000001, 4], 'samsung': [4.533333333333333, 3],
            'xiaomi': [4.366666666666666, 3]}
    assert sort_brands({'apple': [4.800000000000001, 2], 'samsung': [4.5, 2], 'xiaomi': [4.6, 1]}) == \
           {'apple': [4.800000000000001, 2], 'xiaomi': [4.6, 1], 'samsung': [4.5, 2]}
    assert sort_brands({'xiaomi': [4.25, 2], 'apple': [4.3, 2], 'samsung': [4.6, 1]}) == \
           {'samsung': [4.6, 1], 'apple': [4.3, 2], 'xiaomi': [4.25, 2]}

