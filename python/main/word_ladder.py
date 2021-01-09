from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord in wordList:
            ans = 0
            curr = beginWord
            temp = wordList
            #  curr == endWordなら 打ち切り
            while curr != endWord:
                # 1文字違いの単語を探す
                #  ^ の単語を削除して、 ans++
                for i in range(len(temp)):
                    try:
                        if self.check(curr, temp[i]):
                            curr = temp[i]
                            temp.pop(i)
                            ans += 1
                        raise Exception
                    except Exception:
                        pass
            return ans
        else:
            return 0

    def check(self, x: str, y: str) -> bool:
        for i in range(len(x)):
            if x[:i] + x[i + 1 :] == y[:i] + y[i + 1 :]:
                return True
        return False
