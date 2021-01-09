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


def test_check():
    assert Solution().check("hit", "hot") == True
    assert Solution().check("hit", "hog") == False
