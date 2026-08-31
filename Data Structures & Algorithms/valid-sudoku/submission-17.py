class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        blocks = [
            [0, 0], [0, 3], [0, 6],
            [3, 0], [3, 3], [3, 6],
            [6, 0], [6, 3], [6, 6]
        ]

        row_hashmap = {}
        col_hashmap = {}
        block_hashmap = {}
        
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col == '.':
                    continue
                
                row_hashmap[i] = row_hashmap.get(i, defaultdict(int))
                row_hashmap[i][col] = row_hashmap[i].get(col, 0) + 1
                if row_hashmap[i].get(col, 0) > 1:
                    return False
                
                col_hashmap[j] = col_hashmap.get(j, defaultdict(int))
                col_hashmap[j][col] = col_hashmap[j].get(col, 0) + 1
                if col_hashmap[j].get(col, 0) > 1:
                    return False

                block_row = i // 3
                block_col = j // 3
                block_hashmap[block_row, block_col] = block_hashmap.get((block_row, block_col), defaultdict(int))
                block_hashmap[block_row, block_col][col] = block_hashmap[block_row, block_col].get(col, 0) + 1
                if block_hashmap[block_row, block_col][col] > 1:
                    return False

        print(block_hashmap)

        return True
