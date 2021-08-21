import datetime
import os

def intefaz():
    os.system("cls")
    concept=input("""Que fue lo que aprendiste el dia de hoy? 
    """)
    return concept.capitalize()

def timer_calc():
    global now,firt_day,second_day,three_day
    now= datetime.datetime.now()
    firt_day=now + datetime.timedelta(days=2)
    second_day=now + datetime.timedelta(days=7)
    three_day=now + datetime.timedelta(days=30)

def printer():
    print (f"""
    Genial...ahora el momento ideal para repasar "{intefaz()}" son estos momentos:
    """)
    print (f"""El {firt_day.day}/{firt_day.month}/{firt_day.year}
    """)
    print (f"""Luego el {second_day.day}/{second_day.month}/{second_day.year}
    """)
    print (f"""Y por ultimo el {three_day.day}/{three_day.month}/{three_day.year}
    """)


def run():
    timer_calc()
    printer()
    input("Presiona enter para salir!")

if __name__=="__main__":
    run()