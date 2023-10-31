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
Кто живет в {королевство}
Может [имя] жить в [королевство] - может ли [имя] переехать в [королевство]
Помощь - вывести эту строку ещё раз
Выход - завершить работу"""
print(helpstr)

queue = input()
while queue != "Выход":
    if queue.startswith("Какой"):
        l = queue.split(' ')
        name = l[-1]
        print(f'Имя: {name}')
        name = str(name).lower()
        for item in l:
            item = str(item).lower()
            if item == 'у':
                break
            if item == 'возраст':
                q = list(prolog.query(f'age({name},N)'))[0].get('N')
                print(f'Возраст: {q}')
            if item == 'раса':
                q = list(prolog.query(f'race({name},R)'))[0].get('R')
                print(f'Раса: {q}')
            if item == 'королевство':
                q = list(prolog.query(f'where({name}, K'))[0].get('K')
                print(f'Живёт в {str(q).capitalize()}')
            if item == 'профессия':
                q = list(prolog.query(f'proffesion({name}, P)'))[0].get('P')
                print(f'Профессия: {q}')
    elif queue.startswith("Кто живет в"):
        kingdom = queue.split(' ')[-1].lower()
        q = list(prolog.query(f'where(N,{kingdom})'))
        for p in q:
            print(str(p.get('N')).capitalize())
    elif queue.startswith("Может"):
        l = queue.split(" ")
        name = l[1].lower()
        kingdom = l[-1].lower()
        q = list(prolog.query(f'can_move({name}, {kingdom})'))
        ans = handle_tf(q)
        if ans:
            print('Может')
        else:
            do_live = handle_tf(list(prolog.query(f'do_live({name}, {kingdom})')))
            is_king = handle_tf(list(prolog.query(f"is_king({name})")))
            if do_live:
                print('Уже живет здесь')
            elif is_king:
                print('Не может, так как является королём')
            else:
                print('Нарушает рассовый закон')

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
