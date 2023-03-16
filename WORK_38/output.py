def OutputAll():

    with open('file.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line)
       


def Search(data):
    data = data.lower()
    with open('file.txt', 'r', encoding='utf-8') as file:
        flag = False
        for line in file:
            if data in line.lower():
                print(line)
                flag = True
        if flag == False:
            print('\n не найдено \n')



def delete(data):
    lines = open('file.txt', 'r', encoding='utf-8')
    phonebook = lines.readlines()
    for i in range(len(phonebook)):
        if data in phonebook[i]:
            phonebook[i] = ""
    with open('file.txt', 'w', encoding='utf-8') as file:
        file.writelines(phonebook)
        print('Контакт удален')      


# def changes(data):
#      data = open('file.txt', 'r', encoding='utf-8')
#      change = data.readlines()
#      for i in range(len(change)):
        
             
