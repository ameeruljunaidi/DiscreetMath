# We have shown that a position in the 15-puzzle is unsolvable if the corresponding permutation of 15 objects is odd.
# We have not shown yet that the reverse statement is true, i.e., that for every even permutation the puzzle is
# solvable. It is indeed true, and the challenge now is to write a program that produces a sequence of moves for
# every solvable configuration.
#
# Unfortunately, our representation of permutations in python starts with 0, and the numbering of pieces starts with
# 1. To make the output more readable, let us agree that the empty is represented by 0, and the other pieces are
# listed according to their labels in the "reading order", so the standard position is represented as [1, 2, 3, 4, 5,
# 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0] while the impossible configuration we discussed is represented as [1, 2, 3,
# 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 14, 0]. So the position is now represented by a permutation of 0..15,
# and we assume for simplicity that in the initial position the last number (bottom right cell) is 0.
#
# Getting such a sequence as input that corresponds to a solvable configuration, your program should output a
# sequence of moves that transform this configuration into a standard one. Each move is represented by an integer,
# a number on the piece that is moved
#
# For example, you may check that for the position [1, 2, 3, 4, 5, 6, 7, 8, 13, 9, 11, 12, 10, 14, 15, 0] one of the
# solutions is [15, 14, 10, 13, 9, 10, 14, 15]

def main():
    return


if __name__ == "__main__":
    main()
