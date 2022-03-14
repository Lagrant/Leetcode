class TrieNode:
    def __init__(self, val='') -> None:
        self.val = val
        self.children = {}
class AutocompleteSystem:

    def __init__(self, sentences, times):
        self.sentences = sentences
        self.times = times
        self.sent_cnt = {}
        for sent, cnt in zip(self.sentences, self.times):
            self.sent_cnt[sent] = cnt
        
        self.root = TrieNode('')
        self.constructTrie(self.root, self.sentences)
        self.input_node = self.root
        self.input_str = ''
        self.match = True

    def constructTrie(self, root, sentences):
        for sent in sentences:
            cur = root
            for ch in sent:
                if (ch not in cur.children):
                    cur.children[ch] = TrieNode(cur.val + ch)
                    cur = cur.children[ch]
                else:
                    cur = cur.children[ch]
            if ('$' not in cur.children):
                cur.children['$'] = TrieNode(cur.val)
        
    def sort_fit(self, fit):
        for i in range(len(fit)):
            for j in range(i+1, len(fit)):
                if (self.sent_cnt[fit[i]] < self.sent_cnt[fit[j]]):
                    fit[i], fit[j] = fit[j], fit[i]
                elif (self.sent_cnt[fit[i]] == self.sent_cnt[fit[j]] and fit[i] > fit[j]):
                    fit[i], fit[j] = fit[j], fit[i]
    
    def find_prefixes(self, node, fit):
        
        for c in node.children:
            if (c != '$'):
                self.find_prefixes(node.children[c], fit)
                continue
            if (len(fit) < 3):
                fit.append(node.val)
            else:
                self.sort_fit(fit)
                if (self.sent_cnt[fit[-1]] < self.sent_cnt[node.val]):
                    fit[-1] = node.val
                elif (self.sent_cnt[fit[-1]] == self.sent_cnt[node.val] and fit[-1] > node.val):
                    fit[-1] = node.val
    
    def input(self, c: str):
        if (c == '#'):
            if (self.input_str not in self.sent_cnt):
                self.sent_cnt[self.input_str] = 1
                self.constructTrie(self.root, [self.input_str])
            else:
                self.sent_cnt[self.input_str] += 1
            self.input_node = self.root
            self.input_str = ''
            self.match = True
            return []
        
        self.input_str += c
        if (not self.match):
            return []

        fit = []
        for pre in self.input_node.children:
            if (pre == c):
                pre_node = self.input_node.children[pre]
                self.find_prefixes(pre_node, fit)
                break
        
        if (len(fit) > 0):
            self.input_node = self.input_node.children[c]
            self.sort_fit(fit)
            return fit
        else:
            self.match = False
            return []

        
        

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)