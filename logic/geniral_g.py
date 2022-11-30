import logic.bot_moves as lb
import logic.user_moves as lu

ground = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]


def format() -> str:
    global ground

    a = ""
    cnt = 0
    for i in range(len(ground)):
        cnt += 1

        a += ground[i]
        a += " "

        if cnt == 3:
            a += "\n"
            cnt = 0

    return a


def check_check():
    global ground

    if check(ground) == None:
        return None
    else:

        return check(ground)


def check(ground):
    if ground[0] == "O" and ground[1] == "O" and ground[2] == "O" or \
            ground[0] == "O" and ground[3] == "O" and ground[6] == "O" or \
            ground[2] == "O" and ground[5] == "O" and ground[8] == "O" or \
            ground[6] == "O" and ground[7] == "O" and ground[8] == "O" or \
            ground[0] == "O" and ground[4] == "O" and ground[8] == "O" or \
            ground[2] == "O" and ground[4] == "O" and ground[6] == "O" or \
            ground[3] == "O" and ground[4] == "O" and ground[5] == "O" or \
            ground[1] == "O" and ground[4] == "O" and ground[7] == "O":
        return "O win /restart"

    elif ground[0] == "X" and ground[1] == "X" and ground[2] == "X" or \
            ground[0] == "X" and ground[3] == "X" and ground[6] == "X" or \
            ground[2] == "x" and ground[5] == "X" and ground[8] == "X" or \
            ground[6] == "X" and ground[7] == "X" and ground[8] == "X" or \
            ground[0] == "X" and ground[4] == "X" and ground[8] == "X" or \
            ground[2] == "X" and ground[4] == "X" and ground[6] == "X" or \
            ground[3] == "X" and ground[4] == "X" and ground[5] == "X" or \
            ground[1] == "X" and ground[4] == "X" and ground[7] == "X":
        return "X win /restart"

    elif ground[0] != "0" and ground[1] != "1" and ground[2] != "2" and \
            ground[3] != "3" and ground[4] != "4" and ground[5] != "5" and \
            ground[6] != "6" and ground[7] != "7" and ground[8] != "8":
        return "Draw!! /restart"

    else:
        return None


def clear():
    global ground
    ground = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    lu.cnt = 0
    lu.cnt2 = ""
    lu.all_ns = " 012345678"
    lb.cnt = 0
    lb.cnt2 = ""
    lb.all_ns = " 012345678"
