import time
import wincondition as wincon


# Проверка мувмента ладьи
def checklad(deck, pi, pj, fi, fj):
    check = None
    log = ""
    if pi != fi and pj == fj:
        if pi > fi:
            i = fi + 1
            while i < pi:
                if deck[i][pj] != "0":
                    check = 0
                    log = "\n Нельзя перепрыгивать другие фигуры!"
                i += 1
            if check != 0:
                check = 1
        if pi < fi:
            i = fi - 1
            while i > pi:
                if deck[i][pj] != "0":
                    check = 0
                    log = "\n Нельзя перепрыгивать другие фигуры!"
                i -= 1
            if check != 0:
                check = 1
    elif pi == fi and pj != fj:
        if pj > fj:
            j = fj + 1
            while j < pj:
                if deck[pi][j] != "0":
                    check = 0
                    log = "\n Нельзя перепрыгивать другие фигуры!"
                j += 1
            if check != 0:
                check = 1
        if pj < fj:
            j = fj - 1
            while j > pj:
                if deck[pi][j] != "0":
                    check = 0
                    log = "\n Нельзя перепрыгивать другие фигуры!"
                j -= 1
            if check != 0:
                check = 1
    else:
        check = 0
        log = "\n Нельзя так ходить!"
    return check, log


# Проверка мувмента слона
def checksl(deck, fi, fj, pi, pj):
    log = ""
    if abs(fi - pi) == abs(fj - pj):
        if fi > pi:
            mi = -1
        elif fi < pi:
            mi = 1
        else:
            mi = 0
        if fj > pj:
            mj = -1
        elif fj < pj:
            mj = 1
        else:
            mj = 0
        i = fi
        j = fj
        found = 0
        while i != pi and j != pj:
            if deck[i][j] != "0":
                found = 1
            i += mi
            j += mj
        if found == 0:
            check = 1
        else:
            check = 0
            log = "\n Нельзя перепрыгивать другие фигуры!"
    else:
        check = 0
        log = "\n Нельзя так ходить!"
    return check, log


# Функция рокировки
def kingshuffle(deck, fi, fj, pi, pj, face):
    dist = [[2, 1], [1, 2]]
    if pj == dist[face][0]:
        if "5" in deck[pi][0]:
            if dist[face][0] == 2:
                if deck[pi][pj - 1] == "0":
                    check, log = checklad(deck, pi, pj, fi, fj)
                    if check == 1:
                        deck[pi][pj + 1] = deck[pi][0]
                        deck[pi][0] = "0"
                else:
                    check = 0
                    log = "\n Нельзя так проводить рокировку!"
            else:
                check, log = checklad(deck, pi, pj, fi, fj)
                if check == 1:
                    deck[pi][pj + 1] = deck[pi][0]
                    deck[pi][0] = "0"
        else:
            check = 0
            log = "\n Нельзя так проводить рокировку!"
    elif 7 - pj == dist[face][1]:
        if "5" in deck[pi][7]:
            if dist[face][1] == 2:
                if deck[pi][pj + 1] == "0":
                    check, log = checklad(deck, pi, pj, fi, fj)
                    if check == 1:
                        deck[pi][pj - 1] = deck[pi][7]
                        deck[pi][7] = "0"
                else:
                    check = 0
                    log = "\n Нельзя так проводить рокировку!"
            else:
                check, log = checklad(deck, pi, pj, fi, fj)
                if check == 1:
                    deck[pi][pj - 1] = deck[pi][7]
                    deck[pi][7] = "0"
        else:
            check = 0
            log = "\n Нельзя так проводить рокировку!"
    else:
        check = 0
        log = "\n Нельзя так проводить рокировку!"
    return check, log


# Основная функция проверки мувмента (для всех фигур)
def checkmove(deck, face, fi, fj, pi, pj):
    enemfig = [["12", "22", "32", "42", "52", "62", "0"], ["11", "21", "31", "41", "51", "61", "0"]]
    oenemfig = [["12", "22", "32", "42", "52", "62"], ["11", "21", "31", "41", "51", "61"]]
    check = None
    log = ""
    if deck[fi][fj] not in enemfig[face] and deck[pi][pj] in enemfig[face]:
        fig = deck[fi][fj][:len(deck[fi][fj]) // 2]
        if fig == "6":
            if pi in (fi - 2, fi - 1) and pj == fj and deck[pi][pj] == "0":
                if pi == fi - 1:
                    check = 1
                elif pi == fi - 2 and fi == 6:
                    if deck[fi - 1][fj] == "0":
                        check = 1
                    else:
                        check = 0
                        log = "\n Пешка не может перепрыгивать другие фигуры!"
                elif fi != 6:
                    check = 0
                    log = "\n Пешка может так ходить только с начального поля!"
            elif pj in (fj - 1, fj + 1) and pi == fi - 1:
                if deck[pi][pj] in oenemfig[face]:
                    check = 1
                else:
                    check = 0
                    log = "\n Пешка не может ходить по диагонали не атакуя!"
            else:
                check = 0
                log = "\n Пешка не может так ходить!"
        elif fig == "5":
            check, log = checklad(deck, pi, pj, fi, fj)
        elif fig == "4":
            if abs(fi - pi) == 1:
                if abs(fj - pj) == 2:
                    check = 1
                else:
                    check = 0
                    log = "\n Нельзя так ходить!"
            elif abs(fi - pi) == 2:
                if abs(fj - pj) == 1:
                    check = 1
                else:
                    check = 0
                    log = "\n Нельзя так ходить!"
            else:
                check = 0
                log = "\n Нельзя так ходить!"
        elif fig == "3":
            check, log = checksl(deck, fi, fj, pi, pj)
        elif fig == "2":
            check, log1 = checklad(deck, pi, pj, fi, fj)
            if check == 0:
                check, log2 = checksl(deck, fi, fj, pi, pj)
            if log1 != "\n Нельзя так ходить!":
                log = log1
            elif log2 != "\n Нельзя так ходить!":
                log = log2
            else:
                log = log1
        elif fig == "1":
            if abs(fi - pi) == 1 or abs(fj - pj) == 1:
                check, log1 = checklad(deck, pi, pj, fi, fj)
                if check == 0:
                    check, log2 = checksl(deck, fi, fj, pi, pj)
                if log1 != "\n Нельзя так ходить!":
                    log = log1
                elif log2 != "\n Нельзя так ходить!":
                    log = log2
                else:
                    log = log1
            elif fi == pi and abs(fj - pj) == 2:
                check, log = kingshuffle(deck, fi, fj, pi, pj, face)
            else:
                check = 0
                log = "\n Нельзя так ходить!"
    else:
        check = 0
        log = "\n Нельзя выбирать чужую фигуру и/или ходить на поле с вашей фигурой!"
    return check, log


# Функция проверки и обработки ходов
def move(deck, face, fig, pos, score, wc):
    desym = [{"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7},
             {"a": 7, "b": 6, "c": 5, "d": 4, "e": 3, "f": 2, "g": 1, "h": 0}]
    denum = [{"8": 0, "7": 1, "6": 2, "5": 3, "4": 4, "3": 5, "2": 6, "1": 7},
             {"8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1, "1": 0}]
    oenemfig = [["12", "22", "32", "42", "52", "62"], ["11", "21", "31", "41", "51", "61"]]
    figpoints = {"1": 0, "2": 9, "3": 3, "4": 3, "5": 5, "6": 1}
    swapdict = {"1": "2", "2": "5", "3": "4", "4": "3"}
    ch = 0
    fi = 0
    fj = 0
    pi = 0
    pj = 0
    check = 0
    if fig[:len(fig) // 2] in desym[face].keys() and fig[len(fig) // 2:] in denum[face].keys():
        fj = desym[face][fig[:len(fig) // 2]]
        fi = denum[face][fig[len(fig) // 2:]]
    else:
        print("\n Фигура выбрана неправильно!")
        ch = 1
    if pos[:len(pos) // 2] in desym[face].keys() and pos[len(pos) // 2:] in denum[face].keys():
        pj = desym[face][pos[:len(pos) // 2]]
        pi = denum[face][pos[len(pos) // 2:]]
    else:
        print("\n Ход выбран неправильно!")
        ch = 1
    if ch == 0:
        check, log = checkmove(deck, face, fi, fj, pi, pj)
        if check == 1:
            if deck[pi][pj] in oenemfig[face]:
                score[face] += figpoints[deck[pi][pj][:len(deck[pi][pj]) // 2]]
                swap = deck[fi][fj]
            elif deck[fi][fj][:len(deck[fi][fj]) // 2] == "6" and pi == 0:
                swap = input("\n Выберите, на какую фигуру заменить пешку\n Введите одно из чисел:\n Ферзь - 1,"
                             "\n Ладья - 2,\n Конь - 3,\n Слон - 4\n : ")
                done = 0
                while done == 0:
                    if swap in swapdict.keys():
                        swap = f"{swapdict[swap]}{face + 1}"
                        done = 1
                    else:
                        print("\n Фигура выбрана неправильно!")
            else:
                swap = deck[fi][fj]

            deck[pi][pj] = swap
            deck[fi][fj] = "0"
            wc = wincon.wincondition(deck, wc)
        else:
            print(log)
    time.sleep(0.5)
    return deck, check, score, wc
