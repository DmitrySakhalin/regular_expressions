from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)

for i, row in enumerate(contacts_list[1:], start = 1):
  if len(row) >= 3:
    words = row[0].split()
    if len(words) == 3:
      row[0], row[1], row[2] = words[0], words[1], words[2],
    elif len(words) == 2:
      row[0], row[1] = words[0], words[1]


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8", newline="") as f:
  datawriter = csv.writer(f, delimiter=';')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)


