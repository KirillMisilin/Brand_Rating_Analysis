import argparse
import csv
from tabulate import tabulate


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", dest="files", nargs='*')
    parser.add_argument("--report", dest="report")
    return parser.parse_args()


def sort_brands(report):
    sorted_report = dict(sorted(report.items(), key=lambda brand: brand[1], reverse=True))
    return sorted_report


def save_report(report, filename):
    with open(filename + ".csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(report)


def tabulate_to_console(report, target):
    final_report = []
    for row in report:
        final_report.append([row, "%.2f" % report[row][0]])
    headers = ["", "brand", target]
    i = 1
    for row in final_report:
        row.insert(0, i)
        i += 1
    final_report = tabulate(final_report, headers=headers, tablefmt="pretty")
    return final_report


def tabulate_to_file(report, target):
    final_report = [["brand", target]]
    for row in report:
        final_report.append([row, "%.2f" % report[row][0]])
    return final_report


def create_report(target, files):
    if target == "rating":
        target_column = 3
    elif target == "price":
        target_column = 2
    else:
        return None  # если целевой столбец задан неверно, возвращается None
    report = {}
    unique_items = []
    for file in files:
        with open(file, 'r', newline='') as product_file:
            product_reader = csv.reader(product_file, delimiter=',', quotechar='|')
            for row in product_reader:
                full_item_name = row[0] + row[1]
                if full_item_name == "namebrand":  # пропускаем первую строку с заголовками столбцов
                    continue
                # проверка на уникальность имени и бренда. Сделано на случай дубликатов строк в файлах
                if full_item_name not in unique_items:
                    unique_items.append(full_item_name)
                    if row[1] not in report.keys():  # если имя бренда встречается впервые, он добавляется в отчет
                        report[row[1]] = [float(row[target_column]), 1]
                    else:
                        company_rating = report[row[1]][0]  # рейтинг компании на данный момент
                        counter = report[row[1]][1]  # количество повторений компании в файлах для подсчета рейтинга
                        # Обновление среднего рейтинга и количества повторений компании в файлах
                        report[row[1]] = [(company_rating * counter + float(row[target_column]))
                                          / (counter + 1), counter + 1]
                else:
                    pass
    return report


def main():
    target_column = "rating"
    args = parse()  # получение параметров скрипта
    try:
        # Создание отчета. На входе название столбца, для которого нужно найти среднее значение, и название файлов
        report = sort_brands(create_report(target_column, args.files))
        if report:
            file_report = tabulate_to_file(report, target_column)
            save_report(file_report, args.report)
            print(tabulate_to_console(report, target_column))
        else:
            print("Неверное имя строки")
    except FileNotFoundError:
        print("Неверно введены имена файлов")
    except TypeError:
        print("Неверно введено название отчета")


if __name__ == '__main__':
    main()
