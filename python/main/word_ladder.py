from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord in wordList:
            ans = 1
            curr = beginWord
            temp = wordList
            if beginWord in temp:
                temp.remove(beginWord)

            #  curr == endWordなら 打ち切り

            while curr != endWord:
                # 1文字違いの単語を探す
                #  ^ の単語を削除して、 ans++
                try:
                    for i in range(len(temp)):
                        print(curr, temp)
                        t = [x for x in temp if self.check(curr, x)]
                        print(t)
                        if endWord in t:
                            curr = endWord
                            ans += 1
                            print(curr)
                            raise Exception
                        elif len(t) == 0:
                            return 0
                        elif curr == t[0]:
                            print(curr)
                            temp.remove(curr)
                            raise Exception
                        else:
                            s = [x for x in t if self.check(endWord, x)]
                            if len(s) == 0:
                                curr = t[0]
                                print(curr)
                            else:
                                curr = s[0]
                            temp.remove(curr)
                            ans += 1
                            raise Exception
                except Exception:
                    pass
            return ans
        else:
            return 0

    def check(self, x: str, y: str) -> bool:
        def levenshtein_distance(a, b):
            m = [[0] * (len(b) + 1) for i in range(len(a) + 1)]

            for i in range(len(a) + 1):
                m[i][0] = i

            for j in range(len(b) + 1):
                m[0][j] = j

            for i in range(1, len(a) + 1):
                for j in range(1, len(b) + 1):
                    if a[i - 1] == b[j - 1]:
                        x = 0
                    else:
                        x = 1
                    m[i][j] = min(m[i - 1][j] + 1, m[i][j - 1] + 1, m[i - 1][j - 1] + x)
            # print m
            return m[-1][-1]

        return levenshtein_distance(x, y) <= 1


if __name__ == "__main__":
    print(
        Solution().ladderLength(
            "hot",
            "dog",
            ["hot", "dog", "dot"],
        )
    )
