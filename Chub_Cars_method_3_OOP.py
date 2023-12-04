from tabulate import tabulate

f = open("CARS.txt", 'r+')
cars = list()
title = f.readline() #Оглавление таблицы
for i in f:
    cars += [i.split()] #Заполнение списка машин существующими экземплярами

def df(obj):
    test=0
    if obj == 'd':
        text = "Двери открыты? (Да/Нет): "
    elif obj == 'f':
        text = "Фары включены? (Да/Нет): "
    while test==0:
        res = input(text)
        if res != "Да" and res != "да" and res != "Нет" and res != "нет":
            print ("\nОшибка! Введено неверное значение. Введите Да или Нет\n")
        else:
            test=1
    return res

def addcar(nom1,pro1,mod1,dvig1,dver1,far1):
    return [[nom1, pro1, mod1, dvig1, dver1, far1]]

if __name__ == "__main__": 
    a = 0
    while a !='3': #Отображение меню выбора действия
        a = input('МЕНЮ \n1.Список машин \n2.Добавить машину \n3.Выйти\nВведите число: ')
        if a == '1':
            print ('\n\n')
            title1 = title.split()
            counter = 1
            cars1=list()
            for i in cars:
                cars1 += [[str(counter)+'. '] + cars[counter-1]] 
                counter+=1
            print(tabulate(cars1, headers = title1, tablefmt = 'fancy_grid'))#!!!
            
            b = input('\nВыберите машину (введите порядковый номер),\nслово "Поиск" для поиска машины по целому слову/номеру\nили введите "Выход" если хотите выйти в предыдущее меню: ') #Предлагают дальнейшие действия над машинами
            if b == "Выход" or b == "выход":
                print("\nВыходим...\n")
            elif b == "Поиск" or b == "поиск": #Алгоритм поиска по слову
                poisk = str(input("Введите слово или часть слова, чтобы найти подходящие машины: "))
                print("\n")
                counter = 1
                for j in cars:
                    if ' '.join(j).count(poisk)>0:
                        print (str(counter)+ '. ' + ' '.join(j))
                    counter+=1    
                print("\n")
                            
            elif 1<=int(b)<=len(cars):
                print ('\n' + ' '.join(cars[int(b)-1]) + '\n')
                
                c = 0
                while c !='3':
                    c = input ("\nВыберите действие.\n1.Редактировать\n2.Удалить\n3.Выйти\nВведите число: ") #Меню действия над машиной
                    if c == '1':
                        d = 0
                        while d!='4':
                            d = input ("\nЧто хотите отредактировать?.\n1.Двигатель\n2.Двери\n3.Фары\n4.Выход\nВведите число: ")
                            if d == '1':
                                cars[int(b)-1][3] = input ("Введите новый двигатель: ")
                            elif d == '2':
                                cars[int(b)-1][4] = df('d')
                            elif d == '3':
                                cars[int(b)-1][5] = df('f')
                            elif d=='4':
                                break
                            else:
                                print ("\nВведено неверное значение. Попробуйте снова\n")
                                
                    if c == '2': #Удаление и перезапись файла
                        del cars[int(b)-1]
                        with open("CARS.txt", 'w') as fp:
                            fp.write(title)
                            for i in cars:
                                fp.write('\n' + ' '.join(i))
                        break
                    elif c == '3':
                        break
                    else:
                        print("\nВы ввели неверное значение. Повторите попытку.\n")
                
            else:
                print("\nВведено неверное значение. Возврат в главное меню...\n")
            
        elif a == '2':
            nom = input("Введите номер: ")
            pro = input("Введите производителя: ")
            mod = input("Введите модель: ")
            dvig = input("Введите двигатель: ")
            dver = df('d')
            far = df('f')
            cars += addcar(nom,pro,mod,dvig,dver,far)
            f.write('\n' + ' '.join(cars[-1]))
        elif a == '3':
            break
        else:
            print("\nВы ввели неверное значение. Повторите попытку.\n")
    f.close()
    exit()
