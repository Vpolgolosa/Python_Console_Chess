def checkladwc(deck, fi, fj, face):
    oenemfig = [["21", "51"], ["22", "52"]]
    check = 0
    si = [fi + 1, fi - 1, fi, fi]
    sj = [fj, fj, fj + 1, fj - 1]
    mi = [1, -1, 0, 0]
    mj = [0, 0, 1, -1]
    step = 0
    while step < 4:
        i = si[step]
        j = sj[step]
        while 8 > i > -1 and 8 > j > -1:
            if deck[i][j] != "0":
                if deck[i][j] in oenemfig[face]:
                    check = 1
                    break
                else:
                    break
            i += mi[step]
            j += mj[step]
        if check == 0:
            step += 1
        else:
            break
    return check


def checkslwc(deck, fi, fj, face):
    oenemfig = [["21", "31", "61"], ["22", "32", "62"]]
    check = 0
    step = 0
    mi = [1, 1, -1, -1]
    mj = [1, -1, 1, -1]
    while step < 4:
        i = fi
        j = fj
        while 8 > i > -1 and 8 > j > -1:
            i += mi[step]
            j += mj[step]
            if 8 > i > -1 and 8 > j > -1:
                if deck[i][j] != "0":
                    if deck[i][j] in oenemfig[face]:
                        check = 1
                        break
                    else:
                        break
        if check == 0:
            step += 1
        else:
            break
    return check


def checkknwc(deck, fi, fj, face):
    oenemfig = [["41"], ["42"]]
    check = 0
    si = [fi + 2, fi - 2, fi, fi]
    sj = [fj, fj, fj + 2, fj - 2]
    mi = [0, 0, 1, 1]
    mj = [1, 1, 0, 0]
    step = 0
    while step < 4:
        i = si[step]
        j = sj[step]
        if 8 > i + mi[step] > -1 and 8 > j + mj[step] > -1:
            if deck[i + mi[step]][j + mj[step]] != "0":
                if deck[i + mi[step]][j + mj[step]] in oenemfig[face]:
                    check = 1
                    break
        if 8 > i - mi[step] > -1 and 8 > j - mj[step] > -1:
            if deck[i - mi[step]][j - mj[step]] != "0":
                if deck[i - mi[step]][j - mj[step]] in oenemfig[face]:
                    check = 1
                    break
        if check == 0:
            step += 1
        else:
            break
    return check


def wincondition(deck, wc):
    step = 0
    fig = ["12", "11"]
    while step < 2:
        found = 0
        i = 0
        fi = 0
        fj = 0
        check = 0
        while i < 8:
            j = 0
            while j < 8:
                if deck[i][j] == fig[step]:
                    found = 1
                    fi = i
                    fj = j
                    break
                j += 1
            i += 1
        if found == 1:
            check = checkladwc(deck, fi, fj, step)
            if check == 0:
                check = checkslwc(deck, fi, fj, step)
                if check == 0:
                    check = checkknwc(deck, fi, fj, step)
        if wc[step] == 0:
            if check == 1:
                wc[step] = 1
        elif wc[step] == 1:
            if check == 1:
                wc[step] = 2
        step += 1
    return wc