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

    assert Solution().check("hit", "hot") == True
    assert Solution().check("hit", "hog") == False
