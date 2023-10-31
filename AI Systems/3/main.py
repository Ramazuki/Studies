from pyswip import Prolog

prolog = Prolog()
prolog.consult("knowledge_base.pl")


def handle_tf(q):
    if len(q) > 0:
        return True
    return False


helpstr = """Для информации по жителям используйте следующие запросы
Личности - показать все имена
Королевства - показать все королевства
Какой [возраст, профессия, раса, королевство] у [имя] - получить значение свойства данной личности
Кто [младше/старше {число}, расы {название расы (elf, dwarf, human)}, живет в {королевство}, работает {профессия(hunter, knight, king, peasant)}]
Может [имя] жить в [королевство] - может ли [имя] переехать в [королевство]
Помощь - вывести эту строку ещё раз
Выход - завершить работу"""
print(helpstr)

queue = input()
while queue != "Выход":
    if queue.startswith("Какой"):
        pass
    elif queue.startswith("Кто"):
        pass
    elif queue.startswith("Может"):
        l = queue.split(" ")
        name = l[1].lower()
        kingdom = l[-1].lower()
        q = list(prolog.query(f'can_move({name}, {kingdom})'))
        ans = handle_tf(q)
        if ans:
            print('Может')
        else:
            is_king = handle_tf(list(prolog.query(f"is_king({name})")))
            if is_king:
                print('Не может, так как является королём')

    elif queue == "Личности":
        persons = prolog.query("person(Who,_,_,_,_)")
        for person in persons:
            name = str(person.get('Who'))
            print(name.capitalize())
    elif queue == "Королевства":
        kingdoms = prolog.query("kingdom(Name, Law, King)")
        for kingdom in kingdoms:
            name = str(kingdom.get('Name'))
            law = str(kingdom.get('Law'))
            if law.startswith("_"): law = 'Запретов нет'
            king = str(kingdom.get('King'))
            print(f'Королевство {name.capitalize()}\nЗапрет на проживание: {law}\nКороль {king.capitalize()}\n')
    else:
        print('Неверный ввод воспользуйтесь "Помощь"')
    queue = input()
