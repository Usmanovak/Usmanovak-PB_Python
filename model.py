
from copy import deepcopy

#осуществляем ф-ию открыть наши контакты:
phone_book = {}
path = 'phones.txt'
original_pb = {}

def open_file():
    global original_pb
    with open(path, 'r', encoding='UTF-8') as file:
        contacts = file.readlines()
    for contact in contacts:
        uid, name, phone, comment = contact.strip().split(';')        #стрип - убирает ненужные символы
        phone_book[int(uid)] = [name, phone, comment]
    original_pb = deepcopy(phone_book)
#открыли файл на чтение и сделали упорядоченный словарь


#пишем ф-ию присвоения ID к новому контакту:
def next_id():
    return max(phone_book) + 1

#ф-ия добавить контакт:
def add_contact(new: list[str]):
    phone_book[next_id()] = new

#ф-ия сохранить изменения в файле:
def save_file():
    with open(path, 'w', encoding='UTF-8') as file:
        contacts = []
        for uid, contact in phone_book.items():
            contacts.append(';'.join([str(uid), *contact]))
        contacts = '\n'.join(contacts)
        file.write(contacts)

#ф-ия поиска по введенной с клавиатуры строке:
def search(word: str) -> dict[int, list[str]]:
    result = {}
    for uid, contact in phone_book.items():
        if word.lower() in ''.join(contact).lower():
            result[uid] = contact
    return result

#ф-ия замены:
def change(uid: int, new: list[str]) -> str:
    contact = phone_book.get(uid)
    for i in range(3):
        if new[i] != '':
            contact[i] = new[i]
    phone_book[uid] = contact
    return contact[0]

#ф-ия удаления:
def delete (uid: int) -> str:
    return phone_book.pop(uid)[0]