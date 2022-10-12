from leet.longest_palindromic_substring import Solution, SolutionFaster
import pytest


@pytest.fixture
def solution():
    return Solution()


@pytest.fixture
def optimized_solution():
    return SolutionFaster()


def test_base(solution, optimized_solution):
    s = "babad"
    assert solution.longestPalindrome(
        s) == "bab"
    assert optimized_solution.longestPalindrome(s) == "bab"


def test_even_palindrome(solution, optimized_solution):
    s = "cbbd"
    assert solution.longestPalindrome(s) == "bb"
    assert optimized_solution.longestPalindrome(s) == "bb"


def test_whole_palindrome(solution, optimized_solution):
    s = "bb"
    assert solution.longestPalindrome(s) == "bb"
    assert optimized_solution.longestPalindrome(s) == "bb"


def test_one_byte(solution, optimized_solution):
    s = "a"
    assert solution.longestPalindrome(s) == "a"
    assert optimized_solution.longestPalindrome(s) == "a"


def test_finite_runtime(optimized_solution):
    s = "plyvmcthyommabcqtmqklpfkopccabybkneifgjdqhexoezlykccgpfidcqizmotounzpslphlpwghbubwthhpivqvwmvuirfhfnkjzpxyccwnuqodbdmsxybztgzvtonheaxcrpukdpgapfczulexugxghuzuvwqvgckpsgjqyzywlxtzmkqmzgavdmchnyaqzidzjfbizxgikjbsmhyikjvgveeifntxpmpgaoqbzwxyfsnexidvxdxxzzzykphrzprlzoyqqlbxbbgmyzplgqnzphbbdxitexvvjzhtpgkfpfazqiqeyczhkkooykaotkqwuuehbgfyznwjqutbltsamcmzyhzrdvvdrzhyzmcmastlbtuqjwnzyfgbheuuwqktoakyookkhzcyeqiqzafpfkgpthzjvvxetixdbbhpznqglpzymgbbxblqqyozlrpzrhpkyzzzxxdxvdixensfyxwzbqoagpmpxtnfieevgvjkiyhmsbjkigxzibfjzdizqaynhcmdvagzmqkmztxlwyzyqjgspkcgvqwvuzuhgxguxeluzcfpagpdkuprcxaehnotvzgtzbyxsmdbdoqunwccyxpzjknfhfriuvmwvqviphhtwbubhgwplhplspznuotomziqcdifpgcckylzeoxehqdjgfienkbybaccpokfplkqmtqcbammoyhtcmvylp"
    sol = optimized_solution
    res = sol.longestPalindrome(s)
    assert res is not None
