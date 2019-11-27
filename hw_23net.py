print("задача 1 и 2")
input_expression = input("Введите свое выражение (оператор число число) например + 2 2: ")
input_list = input_expression.split(" ")
a = input_list[0]
operator = ["+", "-", "*", "/"]
assert a in operator, print(f"Вы ввели оператор '{a}' - такого оператора нет")

try:
    b = int(input_list[1])
    c = int(input_list[2])
    if a == "+":
        print(b + c)
    elif a == "-":
        print(b - c)
    elif a == "*":
       print(b * c)
    elif a == "/":
        print(b / c)
except(ValueError):
    print("Вы ввели не правильно значение")
except(IndexError):
    print("Вы ввели не все условия для расчета")
except ZeroDivisionError:
    print("На ноль делить нельзя")

print("задача 3. Работа с документами")
#Задача: Расширить домашние задание из лекции 1.4 «Функции — использование встроенных и создание собственных» новой функцией, выводящей имена всех владельцев документов. С помощью исключения KeyError проверяйте, есть ли поле "name" у документа.
#В функции find_owner() я добавил try/expect keyerror. И если в списке documents находится документ у которого нет значения с ключом "name" он возращает текст, что у документа нет владельца. Добавил такой документ руками (номер 1036)
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "insurance", "number": "1036"}
    ]


directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
    }

def find_owner():
  try:
    number = input("Введите номер документа:")
    for document in documents:
      if document["number"] == number:
        name_owner = (document["name"])
        break
      else:
        name_owner = "Не нашел"
    return name_owner
  except KeyError:
    return "У этого документа нет владельца"

def print_list():
  for document in documents:
    print(document["type"], document["number"], document["name"])

def create_new_shelf(new_shelf_number):
  if new_shelf_number in directories:
    print("Такая полка уже есть")
  else:
    directories.update({str(new_shelf_number): []})
    print("Создана полка ", new_shelf_number)

def append_document():
  newdoc_type = input("Введите тип нового документа:")
  newdoc_number = input("Введите номер нового документа:")
  newdoc_owner = input("Введите имя владельца нового документа:")
  while True:
    newdoc_shelf = input("Введите номер полки для нового документа:")
    if not newdoc_shelf in directories:
     new_shelf = input("Такой полки нет, создать? (1 - да, 2 - нет)")
     if new_shelf == "1":
       create_new_shelf(newdoc_shelf)
       directories[newdoc_shelf].append(str(newdoc_number))
       break
     else:
       print("Тогда введи другую полку")
    else:
      print("Полка для документа уже есть. Добавил документ на эту полку.")
      directories[newdoc_shelf].append(str(newdoc_number))
      break
  documents.append({"type": newdoc_type, "number": newdoc_number, "name": newdoc_owner})

def find_shelf(doc_number_for_search):
  for shelf in directories:
    if doc_number_for_search in directories[shelf]:
      shelf_where_doc_rest = str("Документ на полке: " + shelf)
      break
    else:
      shelf_where_doc_rest = "Что-то я не нашел такой документ. Может он где то еще?"
  return shelf_where_doc_rest

def delete_doc():
  doc_number_for_delete = input("Введите номер документа для удаления:")
  for document in documents:
    if document["number"] == doc_number_for_delete:
      result_delete_doc = ("Удалалил документ со следующими значениями: ",document)
      documents.remove(document)
      break
    else:
      result_delete_doc = "Документа с таким номером нет, попробуй еще раз."
  for shelf in directories:
    if doc_number_for_delete in directories[shelf]:
      directories[shelf].remove(doc_number_for_delete)
      result_delete_doc_from_shelf = ("Удалалил документ с полки: ",shelf)
      break
    else:
      result_delete_doc_from_shelf = "Такого документа на полке нет. Может его там не было?"
  return str(str(result_delete_doc) + "\n" + str(result_delete_doc_from_shelf))

def delete_doc_from_shelf(doc_number_for_search):
  for shelf in directories:
    if doc_number_for_search in directories[shelf]:
      directories[shelf].remove(doc_number_for_search)
      result_move_doc_from_shelf = ("Убрал документ с полки: ",shelf)
      break
    else:
      result_move_doc_from_shelf = "Такого документа на полке раньше не было"
  return result_move_doc_from_shelf

def move_old_doc_to_new_shelf(doc_number_for_search):
  if find_shelf(doc_number_for_search) == "Что-то я не нашел такой документ. Может он где то еще?":
    while find_shelf(doc_number_for_search) == "Что-то я не нашел такой документ. Может он где то еще?":
      doc_number_for_search = input("Такого документа нет. Введите номер документа, который мы ищем: ")
    while True:
      new_shelf_for_old_doc = input("Введите номер полки для документа:")
      if not new_shelf_for_old_doc in directories:
        new_shelf = input("Такой полки нет, создать? (1 - да, 2 - нет)")
        if new_shelf == "1":
          create_new_shelf(new_shelf_for_old_doc)
          print(delete_doc_from_shelf(doc_number_for_search))
          directories[new_shelf_for_old_doc].append(str     (doc_number_for_search))
          print("Добавил документ на новую полку ", new_shelf_for_old_doc)
          break
        else:
          print("Тогда введи другую полку")
      else:
        print(delete_doc_from_shelf(doc_number_for_search))
        print("Добавил документ на полку ", new_shelf_for_old_doc)
        directories[new_shelf_for_old_doc].append(str(doc_number_for_search))
        break
  else:
    while True:
      new_shelf_for_old_doc = input("Введите номер полки для документа:")
      if not new_shelf_for_old_doc in directories:
        new_shelf = input("Такой полки нет, создать? (1 - да, 2 - нет)")
        if new_shelf == "1":
          create_new_shelf(new_shelf_for_old_doc)
          print(delete_doc_from_shelf(doc_number_for_search))
          print("Добавил документ на новую полку ", new_shelf_for_old_doc)
          directories[new_shelf_for_old_doc].append(str     (doc_number_for_search))
          break
        else:
          print("Тогда введи другую полку")
      else:
        print(delete_doc_from_shelf(doc_number_for_search))
        print("Добавил документ на полку ", new_shelf_for_old_doc)
        directories[new_shelf_for_old_doc].append(str(doc_number_for_search))
        break

def print_help():
    print("p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит",
          "\nl– list – команда, которая выведет список всех документов в формате passport 2207 876234 Василий Гупкин",
          "\ns – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится",
          "\na – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя",
          "\nas – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень",
          "\nd – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок",
          "\nm – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую",
          "\nh – help – команда, которая выведет на экран эту подсказдку еще раз")

def menu():
  command = input("Введите команду:")
  if command == "p":
    print(find_owner())
  elif command == "l":
    print_list()
  elif command == "a":
    append_document()
  elif command == "s":
    doc_number_for_search = input("Введите номер документа, который мы ищем: ")
    print(find_shelf(doc_number_for_search))
  elif command == "d":
    print(delete_doc())
  elif command == "as":
    new_shelf_number = input("Введите номер полки, которую вы хотите создать: ")
    create_new_shelf(new_shelf_number)
  elif command == "m":
    doc_number_for_search = input("Введите номер документа, который вы хотите перенести: ")
    move_old_doc_to_new_shelf(doc_number_for_search)
  elif command == "h":
    print_help()
  elif command == "e":
    print("Завершаем программу")
    return 1

print_help()
while menu() != 1 :
  menu()