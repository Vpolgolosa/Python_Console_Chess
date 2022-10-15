# 0 - пусто; 1(1,2) - король (белых, черных); 2 - ферзь; 3 - слон; 4 - конь; 5 - ладья; 6 - пешка;
import os
import time

import movement as mov
from random import randint


# Функция очистки экрана
def cls():
    os.system('cls')


# Функия стартовой доски
def startboard():
    deck = [
        ["5", "4", "3", "2", "1", "3", "4", "5"],
        ["6", "6", "6", "6", "6", "6", "6", "6"],
        ["0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0"],
        ["6", "6", "6", "6", "6", "6", "6", "6"],
        ["5", "4", "3", "2", "1", "3", "4", "5"],
    ]
    # deck = [
    #     ["5", "4", "0", "2", "1", "3", "4", "5"],
    #     ["6", "6", "0", "6", "6", "6", "6", "6"],
    #     ["0", "0", "0", "0", "0", "0", "0", "0"],
    #     ["0", "0", "0", "0", "0", "0", "0", "0"],
    #     ["0", "0", "0", "0", "0", "0", "0", "0"],
    #     ["0", "0", "0", "0", "0", "0", "0", "0"],
    #     ["6", "6", "6", "6", "6", "6", "6", "6"],
    #     ["5", "0", "0", "0", "1", "0", "0", "5"],
    # ]
    return deck


# Функция, присваивающая цвет фигурам
def boardp(coin, deck):
    ef = ""
    pf = ""
    if coin == 0:
        ef = "2"
        pf = "1"
    elif coin == 1:
        ef = "1"
        pf = "2"
    p = 0

    for i in deck:
        pp = 0
        for j in i:
            if p <= 1 and deck[p][pp] != "0":
                deck[p][pp] = j + ef
            elif p >= 6 and deck[p][pp] != "0":
                deck[p][pp] = j + pf
            pp += 1
        p += 1
    return deck


# Функция вывода в консоль
def showdeck(deck, face, turn, score, wc):
    cls()
    figures = {"11": "бКр", "12": "чКр", "21": "бФ ", "22": "чФ ", "31": "бС ", "32": "чС ", "41": "бК ", "42": "чК ",
               "51": "бЛ ",
               "52": "чЛ ", "61": "бп ", "62": "чп ", "0": "   "}
    turns = ["черных", "белых"]
    ff = ""
    nu = 0
    tb = ""
    gg = ""
    if wc[0] == 2 and wc[1] != 2:
        gg = "Победа белых!"
    elif wc[1] == 2 and wc[0] != 2:
        gg = "Победа черных!"
    elif wc[0] == 2 and wc[1] == 2:
        gg = "Ничья!"
    if wc[0] == 1 or wc[1] == 1:
        trn = f'\n              Шах!\n        Ход: {turn} | Ход {turns[turn % 2]}\n Счет белых: {score[0]} | Счет черных: {score[1]}\n'
    elif wc[0] != 2 and wc[1] != 2:
        trn = f'\n        Ход: {turn} | Ход {turns[turn % 2]}\n Счет белых: {score[0]} | Счет черных: {score[1]}\n'
    else:
        trn = f'\n         {gg}\n Счет белых: {score[0]} | Счет черных: {score[1]}\n'
    if face == 0:
        tb = f"\n      a     b     c     d     e     f     g     h   \n"
        nu = 8
    elif face == 1:
        tb = f"\n      h     g     f     e     d     c     b     a   \n"
        nu = -1
    p = 0
    for i in deck:
        if p == 0:
            ff += f"{trn}{tb}   +-----+-----+-----+-----+-----+-----+-----+-----+\n"
        pp = 0
        for j in i:
            if j in figures.keys():
                if pp == 0:
                    ff += f' {str(abs(nu - p))} |'
                ff += f' {figures[j]} |'
                if pp == 7:
                    ff += f' {str(abs(nu - p))}'
            pp += 1
        if p == 7:
            ff += f"\n   +-----+-----+-----+-----+-----+-----+-----+-----+{tb}"
        else:
            ff += "\n   +-----+-----+-----+-----+-----+-----+-----+-----+\n"
        p += 1
    print(ff)


# Функция поворота доски
def checkface(deck, state, fa):
    face = 0
    deck2 = deck[:]
    i = 7
    j = 7
    i2 = 0
    j2 = 0
    if state == "s":
        if deck[0][0] == "52":
            face = 0
        elif deck[0][0] == "51":
            face = 1
    elif state == "mi":
        if fa == 0:
            face = 1
        elif fa == 1:
            face = 0
        deck2 = [elem[::-1] for elem in deck][::-1]
    return face, deck2


# Главная функция
def main():
    ga = 0
    while ga != 2:
        deck = startboard()
        # rand = randint(0, 1)
        rand = 0
        wc = [0, 0]
        score = [0, 0]
        deck = boardp(rand, deck)
        face, deck = checkface(deck, "s", 0)
        showdeck(deck, face, 1, score, wc)
        turn = 0
        ga = 0
        while ga != 1:
            turn += 1
            check = 0
            while check == 0:
                fig = input("\n Выберите фигуру: ")
                pos = input("\n Выберите, куда сделать ход: ")
                deck, check, score, wc = mov.move(deck, face, fig, pos, score, wc)
            face, deck = checkface(deck, "mi", face)
            showdeck(deck, face, turn + 1, score, wc)
            time.sleep(0.5)
            if wc[0] == 2 or wc[1] == 2:
                restart = input("\n Введите 1, если хотите играть еще раз\n Введите 2, если хотите выйти из игры: ")
                if restart == "1":
                    ga = 1
                elif restart == "2":
                    ga = 2


# Запуск программы
if __name__ == '__main__':
    main()
