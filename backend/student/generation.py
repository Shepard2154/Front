import random
from datetime import datetime, timedelta
import uuid

from django.contrib.auth.models import User
from loguru import logger

from params.consts import TOMSK_REGIONS, COLLEDGES
from params.parser import save_parse
from params.models import DirectionModel
from .models import StudentModel


LASTNAMES = ["Бонадренко", "Степанюк", "Калиниченко", "Василенко", "Кличко"]

M_NAMES = ['Александр', "Илья", "Никита", "Олег", "Леонид", "Сергей", "Иван", "Максим", "Антон", "Петр"]
M_LASTNAMES = ['Иванов', "Пастухов", "Курчевский", "Бурнаев", "Смирнов", "Мартынов", "Ванифатьев", "Стафеев", "Никулин"] + LASTNAMES
M_FATHERNAMES = ['Сидорович', "Петрович", "Никитич", "Александрович", "Андреевич", "Максимович", "Валерьевич", "Игнатьевич", "Павлович"] 

F_NAMES = ['Александра', "Евгения", "Марина", "Антонина", "Анна", "Светлана", "Юля", "Алена", "Полина", "Валерия"]
F_LASTNAMES = ['Петрова', "Сидорова", "Каренина", "Пастухова", "Смольнякова", "Горяйнова", "Кудряшова", "Тарковская", "Никулина"] + LASTNAMES
F_FATHERNAMES = ['Максимовна', "Александровна", "Петровна", "Сергеевна", "Ивановна", "Олеговна", "Владимировна", "Николаевна", "Леонидовна"] 


def get_random_name():
    male = random.choice(('M', 'F'))
    if male == 'F':
        lastnames = F_LASTNAMES
        names = F_NAMES
        fathername = F_FATHERNAMES
    elif male == 'M':
        lastnames = M_LASTNAMES
        names = M_NAMES
        fathername = M_FATHERNAMES
    return male, random.choice(lastnames), random.choice(names), random.choice(fathername)

def get_random_date(start_year: int, end_year: int) -> datetime:
    return datetime(year=random.choice(range(start_year, end_year)), month=random.choice(range(1,13)), day=random.choice(range(1, 31)))

def gen_student():
    male, lastname, name, fathername = get_random_name()
    date = get_random_date(2000, 2006)
    region = random.choice(TOMSK_REGIONS)
    passport = str(random.randint(1,9))+''.join([str(random.randint(0,9)) for i in range(9)])
    phone = '+7'+random.choice(['8','9'])+''.join([str(random.randint(0,9)) for i in range(9)])
    att_score = random.choice([3, 4]) + random.random()
    is_disabled = random.choice([1, 0])
    is_orphan = random.choice([1, 0])
    is_served = random.choice([1, 0])
    needs_home = random.choice([1, 0])
    is_higher = random.choice([1, 0])
    direction = random.choice(list(DirectionModel.objects.all()))
    academ_duration = random.choice([timedelta(days=random.randint(20, 180)), timedelta()])
    receipt_date = get_random_date(2018, 2020)

    user = User(username=str(uuid.uuid4()))
    user.save()

    StudentModel(male=male, name=name, lastname=lastname, user_model=user, direction=direction,
                is_disabled=is_disabled, is_orphan=is_orphan, is_served=is_served, needs_home=needs_home,
                att_score=att_score, phone=phone, passport=passport, receipt_date=receipt_date,
                birthdate=date, region=region, fathername=fathername, is_higher=is_higher,
                academ_duration=academ_duration).save()

def gen_students(number: int):
    for i in range(number):
        try: gen_student()
        except ValueError: pass



def fill_db():
    save_parse(COLLEDGES)
    gen_students(3000)