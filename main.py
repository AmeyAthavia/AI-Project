# import copy
from io import StringIO
import sys


class MiniMaxOpening:
    def __init__(self):
        self.positions_evaluated = 0
        self.minimax_estimate = 0

    def close_mill(self, loc, board):
        c = board[loc]
        if c == 'W' or c == 'B':
            if loc == 0:
                if board[1] == c and board[2] == c:  # 0
                    return True

            if loc == 1:
                if board[0] == c and board[2] == c:  # 1
                    return True

            if loc == 2:
                if (board[0] == c and board[1] == c) or (board[12] == c and board[21] == c):  # 2
                    return True

            if loc == 3:
                if (board[4] == c and board[5] == c) or (board[8] == c and board[16] == c):  # 3
                    return True

            if loc == 4:
                if board[3] == c and board[5] == c:  # 4
                    return True

            if loc == 5:
                if (board[3] == c and board[4] == c) or (board[11] == c and board[18] == c):  # 5
                    return True

            if loc == 6:
                if board[9] == c and board[13] == c:  # 6
                    return True

            if loc == 7:
                if board[10] == c and board[15] == c:  # 7
                    return True

            if loc == 8:
                if board[3] == c and board[16] == c:  # 8
                    return True

            if loc == 9:
                if board[6] == c and board[13] == c:  # 9
                    return True

            if loc == 10:
                if (board[7] == c and board[15] == c) or (board[11] == c and board[12] == c):  # 10
                    return True

            if loc == 11:
                if (board[10] == c and board[12] == c) or (board[5] == c and board[18] == c):  # 11
                    return True

            if loc == 12:
                if (board[10] == c and board[11] == c) or (board[2] == c and board[21] == c):  # 12
                    return True

            if loc == 13:
                if (board[14] == c and board[15] == c) or (board[6] == c and board[9] == c):  # 13
                    return True

            if loc == 14:
                if (board[13] == c and board[15] == c) or (board[17] == c and board[20] == c):  # 14
                    return True

            if loc == 15:
                if (board[13] == c and board[14] == c) or (board[7] == c and board[10] == c):  # 15
                    return True

            if loc == 16:
                if (board[17] == c and board[18] == c) or (board[3] == c and board[8] == c):  # 16
                    return True

            if loc == 17:
                if (board[16] == c and board[18] == c) or (board[14] == c and board[20] == c):  # 17
                    return True

            if loc == 18:
                if (board[16] == c and board[17] == c) or (board[5] == c and board[11] == c):  # 18
                    return True

            if loc == 19:
                if board[20] == c and board[21] == c:  # 19
                    return True

            if loc == 20:
                if (board[19] == c and board[21] == c) or (board[14] == c and board[17] == c):  # 20
                    return True

            if loc == 21:
                if (board[19] == c and board[20] == c) or (board[2] == c and board[12] == c):  # 21
                    return True

        return False

    def generate_add(self, b):
        ga_list = []
        for i in range(len(b)):
            if b[i] == 'x':
                copy_board = b.copy()
                copy_board[i] = 'W'
                if self.close_mill(i, copy_board):
                    ga_list = self.generate_remove(copy_board, ga_list)
                else:
                    ga_list.append(copy_board)
        return ga_list

    def generate_remove(self, b, lst):
        gr_list = lst.copy()
        for i in range(len(b)):
            if b[i] == 'B':
                if not self.close_mill(i, b):
                    cbo = b.copy()
                    cbo[i] = 'x'
                    gr_list.append(cbo)
                else:
                    cbo = b.copy()
                    gr_list.append(cbo)
        return gr_list

    def static_estimation(self, s_board):
        w_count = 0
        b_count = 0
        for i in range(len(s_board)):
            if s_board[i] == 'W':
                w_count += 1
            elif s_board[i] == 'B':
                b_count += 1
        return w_count - b_count

    def maxmin(self, x, depth):
        if depth > 0:
            print("current depth at maxmin is", depth)
            depth -= 1
            children = self.generate_add(x)
            for c in children:
                print("the possible moves for white are:", ''.join(c))
            v = -999999
            maxboardchoice = [None] * 50
            for i in range(len(children)):
                minboard = self.minmax(children[i], depth)
                if v < self.static_estimation(minboard):
                    v = self.static_estimation(minboard)
                    # global self.minimax_estimate
                    self.minimax_estimate = v
                    maxboardchoice = children[i]
            return maxboardchoice
        elif depth == 0:
            # global positions_evaluated
            self.positions_evaluated += 1
        return x

    def minmax(self, x, depth):
        if depth > 0:
            print("current depth at minmax is", depth)
            depth -= 1
            bchildren = self.generateBlackMoves(x)
            for bc in bchildren:
                print("the possible moves for black are:", ''.join(bc))
            v = 999999
            minboardchoice = [None] * 50
            for i in range(len(bchildren)):
                maxBoard = self.maxmin(bchildren[i], depth)
                if v > self.static_estimation(maxBoard):
                    v = self.static_estimation(maxBoard)
                    minboardchoice = bchildren[i]
            return minboardchoice
        elif depth == 0:
            # global positions_evaluated
            self.positions_evaluated += 1
        return x

    def swapWB(self, x):
        lboard = x.copy()
        for i in range(len(lboard)):
            if lboard[i] == 'W':
                lboard[i] = 'B'
                continue
            if lboard[i] == 'B':
                lboard[i] = 'W'
        return lboard

    def generateBlackMoves(self, x):
        lboard = x.copy()
        for i in range(len(lboard)):
            if lboard[i] == 'W':
                lboard[i] = 'B'
                continue
            if lboard[i] == 'B':
                lboard[i] = 'W'
        gbm = self.generate_add(lboard)
        gbmswap = []
        for y in gbm:
            gbmswap.append(self.swapWB(y))
        return gbmswap


if __name__ == '__main__':
    fInputFile = sys.argv[1]
    fOutputFile = sys.argv[2]
    depth = int(sys.argv[3])

    try:
        with open(fInputFile, 'r') as fis:
            with open(fOutputFile, 'w') as out:
                s = StringIO(fis.read())

                while True:
                    st = s.readline()
                    if not st:
                        break
                    b = list(st.strip())
                    m = MiniMaxOpening()
                    print("given board : ", "".join(b))
                    e = m.swapWB(b)
                    print("".join(e))
                    d = m.maxmin(b, depth)
                    print(m.positions_evaluated)
                    print(m.minimax_estimate)
                    out.write("Board Position : " + "".join(d) + "\n")
                    out.write("Positions evaluated by static estimation : " + str(m.positions_evaluated) + "\n")
                    out.write("MiniMax estimate : " + str(m.minimax_estimate) + "\n")
    except IOError as e:
        print(e)
