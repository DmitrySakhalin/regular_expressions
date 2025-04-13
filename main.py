import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

pattern = r"(\+7|8)\s*[(]*(\d{3})[)]*[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})\s*(?:доб\.?\s*(\d+))?"

contacts_dict = {}

for contact in contacts_list[1:]:
    if len(contact) > 2:
        fullname = " ".join(contact[:3]).split()  # Соединяем три первых элемента, затем разделяем по пробелам
        lastname = fullname[0] if len(fullname) > 0 else ""
        firstname = fullname[1] if len(fullname) > 1 else ""
        surname = fullname[2] if len(fullname) > 2 else ""
    else:
        lastname = contact[0]
        firstname = ""
        surname = ""

    fio_key = (lastname, firstname)

    organization = contact[3] if len(contact) > 3 else ""
    position = contact[4] if len(contact) > 4 else ""
    phone = contact[5] if len(contact) > 5 else ""
    email = contact[6] if len(contact) > 6 else ""

    if phone:
        match = re.match(pattern, phone)
        if match:
            formatted_phone = f"+7({match.group(2)}){match.group(3)}-{match.group(4)}-{match.group(5)}"

            if len(match.groups()) > 5 and match.group(6):
                formatted_phone += f" доб.{match.group(6)}"

            phone = formatted_phone

    if fio_key not in contacts_dict:
        contacts_dict[fio_key] = [lastname, firstname, surname, organization, position, phone, email]
    else:
        existing_contact = contacts_dict[fio_key]
        existing_contact[2] = surname if surname else existing_contact[2]
        existing_contact[3] = organization if organization else existing_contact[3]
        existing_contact[4] = position if position else existing_contact[4]
        existing_contact[5] = phone if phone else existing_contact[5]
        existing_contact[6] = email if email else existing_contact[6]

final_contacts = list(contacts_dict.values())

header = ["Фамилия", "Имя", "Отчество", "Организация", "Должность", "Телефон", "Email"]
final_contacts.insert(0, header)

with open("phonebook.csv", "w", encoding="utf-8-sig", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(final_contacts)
