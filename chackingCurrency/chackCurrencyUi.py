#from PyQt5 import QtWidgets
import tkinter as tk
import file_pb2
person = file_pb2.Person()
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"
phone = person.phones.add()
phone.number = "555-4321"
phone.type = file_pb2.Person.HOME

print(person.number)




