from collections import defaultdict
class TrieNode:
    def __init__(self, val='', child={}) -> None:
        self.val = val
        self.child = child


class Solution:
    def __init__(self) -> None:
        self.board = None
        self.w_map = defaultdict(list)
        self.dirs = [[-1,0], [1,0], [0,-1], [0,1]]
        self.ans = []
        self.word_dict = defaultdict(int)

    def insert(self, root, word) -> None:
        cur = root
        for w in word:
            if (w not in cur.child):
                cur.child[w] = TrieNode(w, {})
                cur.child[w].val = cur.val + w
                cur = cur.child[w]
            else:
                cur = cur.child[w]


    def travserse(self, root):
        ws = [w for w in root.child]
        # for w in root.child:
        for w in ws:
            if (w not in self.w_map or w not in root.child):
                continue
            visited = defaultdict(bool)
            for pos in self.w_map[w]:
                if (w not in root.child):
                    break
                self.trav(root.child[w], root, pos, visited)
    def trav(self, node, parent, pos, visited):
        visited[','.join([str(i) for i in pos])] = True
        for dir in self.dirs:
            new_pos = [pos[i] + dir[i] for i in range(len(pos))]
            if (new_pos[0] < 0 or new_pos[0] >= len(self.board) or new_pos[1] < 0 or new_pos[1] >= len(self.board[0])):
                continue
            new_pos_str = ','.join([str(i) for i in new_pos])
            if (visited[new_pos_str]):
                continue
            if (self.board[new_pos[0]][new_pos[1]] in node.child):
                self.trav(node.child[self.board[new_pos[0]][new_pos[1]]], node, new_pos, visited)
        # for w in node.child:
        #     for dir in self.dirs:
        #         new_pos = [pos[i] + dir[i] for i in range(len(pos))]
        #         if (new_pos[0] < 0 or new_pos[0] >= len(self.board) or new_pos[1] < 0 or new_pos[1] >= len(self.board[0])):
        #             continue
        #         new_pos_str = ','.join([str(i) for i in new_pos])
        #         if (visited[new_pos_str]):
        #             continue
        #         if (self.board[new_pos[0]][new_pos[1]] == w):
        #             if (self.trav(node.child[w], node, new_pos, visited)):
        #                 break
        
        visited[','.join([str(i) for i in pos])] = False
        if (node.val in self.word_dict):
            if (self.word_dict[node.val] == 0):
                self.ans.append(node.val)
                self.word_dict[node.val] = 1
            if (not any(node.child)):
                parent.child.pop(node.val[-1])
            return True
        else:
            return False
    
    def findWords(self, board, words):
        # ans = []
        self.board = board
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self.w_map[self.board[i][j]].append([i, j])
        
        root = TrieNode(val='', child={})
        for w in words:
            self.insert(root, w)
            self.word_dict[w] = 0

        self.travserse(root)



        return self.ans



sol = Solution()
# print(sol.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))
print(sol.findWords([['a', 'a']],  ['a']))

class Solution1:
    def findWords(self, board, words):
        WORD_KEY = '$'
        
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word
        
        rowNum = len(board)
        colNum = len(board[0])
        
        matchedWords = []
        
        def backtracking(row, col, parent):    
            
            letter = board[row][col]
            currNode = parent[letter]
            
            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                matchedWords.append(word_match)
            
            # Before the EXPLORATION, mark the cell as visited 
            board[row][col] = '#'
            
            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset     
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)
        
            # End of EXPLORATION, we restore the cell
            board[row][col] = letter
        
            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)
        
        return matchedWords  