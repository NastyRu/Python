# Редактирование текста

# Сиденко Анастасия, ИУ7-13Б

text = ['Ведь, если звезды зажигают -', 'Значит - кто-то называет эти плевочки.']
alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
sogl = 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩъьбвгджзйклмнпрстфхцчшщЪЬ'
znak = '.!?'
txt = '01234'
for stroka in text:
    print(stroka)
print()
F = True
E = True
while F:
    if E:
        print('Что надо сделать?')
        print('1.Удалить заданное слово во всем тексте')
        print('2.Произвести замену одного слова другим')
        print('3.Отформатировать текст')
        print('4.Найти слово в самом длинном предложении, где меньше всего согласных')
        print('0.Выйти')
    x = input()
    print()
    textnov = []
    if (x in txt) == 0:
        print('Некорректный ввод. Повторите попытку.')
        E = False
    else:
        x=int(x)
        E = True
    if x == 0:
        F = False
    if x == 1:
        slovo = input('Введите слово ')
        j = k = l = 0
        for stroka in text:
            j = k = l = 0
            strokanov = ''
            for i in range(len(stroka)): 
                if ((stroka[i].upper() in alf)==0):
                    if (l != k) or (l != j):
                        for q in range(i-l,i):
                            strokanov+=stroka[q]    
                    strokanov+=stroka[i]
                    j = k = l = 0
                elif j>=len(slovo):
                    l+=1
                elif (stroka[i].upper() in alf) and \
                     (stroka[i].lower()==slovo[j].lower()):
                    k+=1
                    l+=1
                    j+=1
                else:
                    l+=1
            textnov.append(strokanov)
            text = textnov
    if x == 2:
        zam = input('Введите слово, которое нужно заменить ')
        nov = input('Введите слово, на которое нужно заменить ')
        j = k = l = 0
        for stroka in text:
            j = k = l = 0
            strokanov = ''
            for i in range(len(stroka)): 
                if (stroka[i].upper() in alf)==0:
                    if (l != k) or (l != j):
                        for q in range(i-l,i):
                            strokanov+=stroka[q]
                    if (l==k) and (l==j) and (j>0):
                        strokanov+=nov
                    strokanov+=stroka[i]
                    j = k = l = 0
                elif j>=len(zam):
                    l+=1
                elif (stroka[i].upper() in alf) and \
                     (stroka[i].lower()==zam[j].lower()):
                    k+=1
                    l+=1
                    j+=1
                else:
                    l+=1
            textnov.append(strokanov)
            text = textnov
    if x == 3:
        print('Выберите как отформатировать текст ')
        print('1.По левому краю')
        print('2.По ширине')
        print('3.По правому краю')
        t = int(input())
        if t == 1:
            for stroka in text:
                textnov.append(stroka.lstrip())
        if t == 3:
            maxlen = 0
            for stroka in text:
                if len(stroka)>maxlen:
                    maxlen = len(stroka)
            for stroka in text:
                strokanov = ' '*(maxlen-len(stroka))
                strokanov+=stroka
                textnov.append(strokanov)
        if t == 2:
            maxlen = 0
            for stroka in text:
                if len(stroka)>maxlen:
                    maxlen = len(stroka)                    
            for stroka in text:
                k = maxlen-len(stroka)
                word = stroka.split()
                i=1
                if len(word)>1:
                    while k>0:
                        k-=1
                        word[i%(len(word)-1)]+=' '
                        i+=1
                sep=' '
                textnov.append(sep.join(word))
    if x == 4:
        slovo=''
        lenpredl = lenpredlmax = kolsogl = imax = imin = toc = num = 0
        kolsoglmin = [len(sogl)]*7
        slovomin = ['']*6
        for stroka in text:
            for i in range(len(stroka)):
                lenpredl+=1
                if stroka[i] in sogl:
                    kolsogl+=1
                if ((stroka[i] in znak) or (stroka[i] == ' ')) and \
                   (stroka[i-1].upper()in alf):
                    if kolsogl<kolsoglmin[toc]:
                        kolsoglmin[toc]=kolsogl
                        slovomin[toc]=slovo
                    slovo=''
                    kolsogl=0
                if stroka[i] in znak:
                    toc+=1
                    if lenpredl>lenpredlmax:
                        lenpredlmax=lenpredl
                        imax=toc
                        num = text.index(stroka)
                    lenpredl=0
                if stroka[i].upper() in alf:
                    slovo+=stroka[i]
        print(slovomin[imax-1])
    if (x == 1) or (x == 2):
        print('\nПОЛУЧЕННЫЙ ТЕКСТ:')
        for stroka in text:
            print(stroka)
    if (x == 3):
        print('\nПОЛУЧЕННЫЙ ТЕКСТ:')
        for stroka in textnov:
            print(stroka)
    print()
