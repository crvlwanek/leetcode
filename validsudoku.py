# 36. Valid Sudoku

def isValidSudoku(self, board: List[List[str]]) -> bool:

  def new_set() -> set[str]:
    return {str(n) for n in range(1, 10)}

  def is_in_set(value: str, _set: set[str]) -> bool:
    if value == '.':
      return True
    if value not in _set:
      return False
    _set.remove(value)
    return True

  def rows_cols_are_valid() -> bool:

    for i in range(9):
      set1 = new_set()
      set2 = new_set()
      for j in range(9):
        if not (is_in_set(board[i][j], set1) and is_in_set(board[j][i], set2)):
          return False

    return True

  def squares_are_valid() -> bool:

    starting_points = [
      (0, 0), (0, 3), (0, 6),
      (3, 0), (3, 3), (3, 6),
      (6, 0), (6, 3), (6, 6)
    ]

    for y, x in starting_points:
      _set = new_set()
      for i in range(y, y + 3):
        for j in range(x, x + 3):
          if not is_in_set(board[i][j], _set):
            return False

    return True

  return rows_cols_are_valid() and squares_are_valid()
  
  
