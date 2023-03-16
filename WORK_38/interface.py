while True:
    choise = int(input('Введите нужное действие: \n 1 - Добавить в справочник \
        \n 2 - Вывести всех \n 3 - Поиск по фамилии \n 4 - Удалить информацию \
        \n 5 - Изменить данные  \n 6 - Выход\n'))
    match choise: 
        case 1: 
            import input1
            input1.Input(input('Введите имя: '), input('Введите номер: '))
        case 2: 
            from output import OutputAll
            OutputAll()
        case 3:
            from output import Search
            Search(input('Введите фамилию: '))
        case 4:
            from output import delete
            delete(input('Введите имя или фамилию: '))
        case 5:
            from output import changes
            changes(input('Введите имя или фамилию: '))
        case 6: break