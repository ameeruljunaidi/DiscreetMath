# Write a Python function solution(position) that gets a (solvable) position in 15-puzzle and outputs a sequence of
# moves that transforms it to a standard position. See in the previous Reading item about encodings. In short,
# position is a sequence of integers written in the cells, where empty cell is represented by 0; moves in the
# sequence are labels on the cells that move.

from typing import List
from copy import copy

row_length: int = 4
board_size: int = 16
end_grid: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]


class Node:
    def __init__(self, flat_grid: List[int]):
        self.flat_grid: List[int] = flat_grid
        self.seq_counter: int = 0
        self.misplaced_tiles: int = self.get_misplaced_tiles()
        self.f_value: int = self.seq_counter + self.misplaced_tiles
        self.zero_index: int = self.get_zero_index()
        self.movable_indices: List[int] = self.get_indices()

    def get_zero_index(self) -> int:
        return self.flat_grid.index(0)

    def solved(self) -> bool:
        """
        Need to know if the board has already been solved or not, if we know it's not been solved, then need to keep
        working If it is already solved, then we can stop :return: true or false depending on if the node is already
        solved or not
        """

        for i in range(board_size):
            if self.flat_grid[i] != end_grid[i]:
                return False

        return True

    def solvable(self) -> bool:
        """
        Need to know if the board is solvable or not
        :return: true if board is solvable, false if not
        """
        moves: int = 0

        for i in range(board_size):
            if self.flat_grid[i] != i:
                self.flat_grid[self.flat_grid.index(i)] = self.flat_grid[i]
                self.flat_grid[i] = i
                moves += 1

        if moves % 2 == 0:
            return True

        return False

    def get_misplaced_tiles(self) -> int:
        counter: int = 0

        for i in range(board_size):
            if self.flat_grid[i] != end_grid[i]:
                counter += 1

        return counter

    def get_index(self, direction: str) -> int:
        """
        We need to figure out which index can transpose with the zero element
        :param direction: up, down, right, or left of the zero element
        :return: -1 if the index does not exist, index of the element if it is possible
        """

        zero_index: int = self.zero_index

        if direction == "up":
            return zero_index - row_length if zero_index - row_length >= 0 and zero_index != -1 else -1
        elif direction == "down":
            return zero_index + row_length if zero_index + row_length < board_size and zero_index != -1 else -1
        elif direction == "right":
            return zero_index + 1 if zero_index % row_length < row_length - 1 and zero_index != -1 else -1
        elif direction == "left":
            return zero_index - 1 if zero_index % row_length >= 1 and zero_index != -1 else -1

        return -1

    def get_indices(self) -> List[int]:
        directions: List[str] = ["up", "down", "right", "left"]
        indices: List[int] = [self.get_index(direction) for direction in directions if self.get_index(direction) != -1]

        return indices

    def swap(self, index: int) -> int:
        ret_index: int = self.flat_grid[index]

        self.flat_grid[self.zero_index] = self.flat_grid[index]
        self.flat_grid[index] = 0
        self.zero_index = index
        self.seq_counter += 1
        self.misplaced_tiles = self.get_misplaced_tiles()
        self.f_value = self.seq_counter + self.misplaced_tiles
        self.movable_indices = self.get_indices()

        return ret_index


class Solution:
    def __init__(self, start_grid: Node):
        self.start_grid: Node = start_grid
        self.movements: List[int] = []

    def solve(self):
        grid: Node = copy(self.start_grid)  # Copy the start grid
        visited_states: List[List[int]] = []

        while grid.solved:
            temp_grid: Node = copy(grid)
            temp_f_value: int = 0
            moved_tile: int = -1

            for index in grid.movable_indices:
                temp_moved_tile: int = temp_grid.swap(index)

                if temp_f_value == 0 and moved_tile == -1 and temp_grid.flat_grid not in visited_states:
                    temp_f_value = temp_grid.f_value
                    moved_tile = temp_moved_tile
                else:
                    if temp_f_value < temp_grid.f_value and temp_grid.flat_grid not in visited_states:
                        temp_f_value = temp_grid.f_value
                        moved_tile = temp_moved_tile

            grid = copy(temp_grid)
            visited_states.append(copy(grid.flat_grid))
            self.movements.append(moved_tile)


def main():
    start_grid: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 13, 9, 11, 12, 10, 14, 15, 0]
    problem: Node = Node(start_grid)
    solution: Solution = Solution(problem)

    if not solution.start_grid.solvable:
        print("Problem not solvable.")
        exit()

    solution.solve()
    print(solution.movements)

    return


if __name__ == '__main__':
    main()
