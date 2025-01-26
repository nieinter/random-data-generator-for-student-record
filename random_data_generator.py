import datetime
import pymongo
import bcrypt
from random import choice

# pymongo.MongoClient("mongodb://localhost:27017/")["grades_db"]["lesson_journal"].drop()
# pymongo.MongoClient("mongodb://localhost:27017/")["grades_db"]["login_data"].drop()

grades_amount = 40

grades = ('-6', '-5', '-4', '-3', '-2', '+5', '+4', '+3', '+2', '+1', '6', '5', '4', '3', '2', '1')

subjects = ("Matematyka",
            "Biologia",
            "Język angielski",
            "Język polski",
            "Język niemiecki",
            "Język francuski",
            "Język łaciński",
            "Informatyka",
            "WF",
            "Chemia",
            "Historia",
            "Fizyka",
            "Religia",
            "Geografia",
            "WOS")

weights = {"Kartkówka": 2,
           "Odpowiedź ustna": 1,
           "Sprawdzian": 3,
           "Praca dodatkowa": 1,
           "Konkurs": 4,
           "Aktywność": 1}


def random_grades(uid):
    col_grades = pymongo.MongoClient("mongodb://localhost:27017/")["grades_db"]["lesson_journal"]
    for _ in range(grades_amount):
        rand = choice(list(weights.keys()))
        col_grades.insert_one({"uid": str(uid),
                               "Przedmiot": choice(subjects),
                               "Ocena": choice(grades),
                               "Waga": weights[rand],
                               "Opis": rand,
                               "Data": datetime.datetime.now().strftime("%d/%m/%Y")})


col_login = pymongo.MongoClient("mongodb://localhost:27017/")["grades_db"]["login_data"]

password = bcrypt.hashpw("password1".encode("utf-8"), bcrypt.gensalt())
col_login.insert_one({"Login": "student1", "Password": password.decode("utf-8")})
password = bcrypt.hashpw("password2".encode("utf-8"), bcrypt.gensalt())
col_login.insert_one({"Login": "student2", "Password": password.decode("utf-8")})

for i in col_login.find():
    random_grades(i["_id"])
