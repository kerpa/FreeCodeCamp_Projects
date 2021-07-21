value_stop = 1


def decoupage_list(a):
    ope = []
    taille = len(a)

    for n in range(taille):
        storage = a[n]
        ope = ope + storage.split()
    return ope


def affichage(liste_entree):
    taille = len(liste_entree)

    operations = []

    premiere_ligne = ''
    deuxieme_ligne = ''

    def first_line(x):
        f = len(x)
        spaces1 = 7 - f
        return spaces1 * ' ' + x

    def second_line(y):
        g = len(y)
        spaces2 = 4 - g
        return spaces2 * ' ' + y

    operations = decoupage_list(liste_entree)

    for i1 in range(0, len(operations), 3):
        premiere_ligne = premiere_ligne + first_line(operations[i1]) + ' ' * 3
    premiere_ligne = premiere_ligne + "\n"
    # print(premiere_ligne)

    for i2 in range(1, len(operations), 3):
        deuxieme_ligne = deuxieme_ligne + ' ' + operations[i2] + ' ' + ' ' * (
                1 - len(operations[i2 + 1])) + second_line(operations[i2 + 1]) + '   '

    deuxieme_ligne = deuxieme_ligne + "\n"
    # print(deuxieme_ligne)

    ligne_egal = ' ------   ' * taille + "\n"
    # print(' ------   '* taille)

    total = premiere_ligne + deuxieme_ligne + ligne_egal
    return total


def check_sign(a):

    b = ['*', '/']
    c = decoupage_list(a)

    for n in range(1, len(c), 3):
        if c[n] == b[0]:
            print("Error: Operator must be '+' or '-'.")
            return 1
        elif c[n] == b[1]:
            print("Error: Operator must be '+' or '-'.")
            return 1

    return 0


def check_longueur(x):
    y = decoupage_list(x)

    for n in range(0, len(y), 3):
        if len(y[n]) > 4:
            print("Error: Numbers cannot be more than four digits.")
            return 1

    for n in range(2, len(y), 3):
        if len(y[n]) > 4:
            print("Error: Numbers cannot be more than four digits.")
            return 1

    if len(x) > 5:
        print("Error: Too many problems.")
        return 1

    return 0


def check_nombre(x):

    y = decoupage_list(x)

    for n in range(0, len(y), 3):
        try:
            int(y[n])
        except:
            print("Error: Numbers must only contain digits.")
            return 1

    for n in range(2, len(y), 3):
        try:
            int(y[n])
        except:
            print('Error: Numbers must only contain digits.')
            return 1

    return 0


def resultant(a):
    l1 = []
    l2 = ''

    for n in range(len(a)):
        l1.append(eval(a[n]))

    for i in range(len(l1)):
        c = str(l1[i])
        l2 = l2 + ' ' * (7 - len(c)) + c + ' ' * 3

    # print(l2)
    return l2 + '\n'


def arithmetic_arranger(a, result):

    if not result:
        if check_nombre(a) != value_stop and check_longueur(a) != value_stop and check_sign(a) != value_stop:
            return affichage(a)
    if check_nombre(a) != value_stop and check_longueur(a) != value_stop and check_sign(a) != value_stop:
        return affichage(a) + resultant(a)


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
