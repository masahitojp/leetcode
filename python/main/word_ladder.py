from typing import List, Set


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set: Set[str] = set(wordList)
        count: int = 1
        prev: List[int] = [beginWord]
        while len(prev) != 0:
            count += 1
            next = []
            for word in prev:
                for i in range(0, len(word)):
                    prefix: str = word[:i]
                    suffix: str = word[(i + 1) :]
                    for c in range(ord("a"), ord("z") + 1):
                        next_word = prefix + chr(c) + suffix
                        if not (next_word in word_set):
                            continue
                        if next_word == endWord:
                            return count
                        word_set.remove(next_word)
                        next.append(next_word)
            # print(count, next, word_set)
            prev = next
        return 0


if __name__ == "__main__":
    Solution().ladderLength(
        "qa",
        "sq",
        [
            "si",
            "go",
            "se",
            "cm",
            "so",
            "ph",
            "mt",
            "db",
            "mb",
            "sb",
            "kr",
            "ln",
            "tm",
            "le",
            "av",
            "sm",
            "ar",
            "ci",
            "ca",
            "br",
            "ti",
            "ba",
            "to",
            "ra",
            "fa",
            "yo",
            "ow",
            "sn",
            "ya",
            "cr",
            "po",
            "fe",
            "ho",
            "ma",
            "re",
            "or",
            "rn",
            "au",
            "ur",
            "rh",
            "sr",
            "tc",
            "lt",
            "lo",
            "as",
            "fr",
            "nb",
            "yb",
            "if",
            "pb",
            "ge",
            "th",
            "pm",
            "rb",
            "sh",
            "co",
            "ga",
            "li",
            "ha",
            "hz",
            "no",
            "bi",
            "di",
            "hi",
            "qa",
            "pi",
            "os",
            "uh",
            "wm",
            "an",
            "me",
            "mo",
            "na",
            "la",
            "st",
            "er",
            "sc",
            "ne",
            "mn",
            "mi",
            "am",
            "ex",
            "pt",
            "io",
            "be",
            "fm",
            "ta",
            "tb",
            "ni",
            "mr",
            "pa",
            "he",
            "lr",
            "sq",
            "ye",
        ],
    )
