from typing import List


def is_even(v: List[int]) -> bool:
    moves: int = 0
    for i in range(len(v)):

        if v[i] != i:
            v[v.index(i)] = v[i]
            v[i] = i
            moves += 1

        else:
            continue

    if moves % 2 == 0:
        return True

    return False


def main():
    v1: List[int] = [5, 2, 9, 1, 6, 4, 7, 0, 8, 3, 10]
    v2: List[int] = [0, 4, 1, 3, 5, 2]

    ans1: str = "Even" if (is_even(v1)) else "Odd"
    ans2: str = "Even" if (is_even(v2)) else "Odd"

    print("Case 1:", ans1)  # Odd
    print("Case 2:", ans2)  # Odd


if __name__ == '__main__':
    main()
