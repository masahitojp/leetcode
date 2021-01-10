from main.word_ladder import Solution


def test_ladderLength():
    assert (
        Solution().ladderLength(
            beginWord="hit",
            endWord="cog",
            wordList=["hot", "dot", "dog", "lot", "log", "cog"],
        )
        == 5
    )
    assert (
        Solution().ladderLength(
            beginWord="hit",
            endWord="cog",
            wordList=["hot", "dot", "dog", "lot", "log"],
        )
        == 0
    )
    assert (
        Solution().ladderLength(
            beginWord="a",
            endWord="c",
            wordList=["a", "b", "c"],
        )
        == 2
    )
    assert (
        Solution().ladderLength(
            beginWord="hot",
            endWord="dog",
            wordList=["hot", "dog"],
        )
        == 0
    )
    assert (
        Solution().ladderLength(
            "hot",
            "dog",
            ["hot", "cog", "dog", "tot", "hog", "hop", "pot", "dot"],
        )
        == 3
    )
    assert (
        Solution().ladderLength(
            "hit",
            "cog",
            ["hot", "hit", "cog", "dot", "dog"],
        )
        == 5
    )

    assert (
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
        == 5
    )
    assert (
        Solution().ladderLength(
            "kiss",
            "tusk",
            [
                "miss",
                "dusk",
                "kiss",
                "musk",
                "tusk",
                "diss",
                "disk",
                "sang",
                "ties",
                "muss",
            ],
        )
        == 5
    )
