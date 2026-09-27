from typing import List

def letterCombinations(digits: str) -> List[str]:
    if not digits:
        return []

    phone = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }

    ans = []
    tempans = []

    def backtrack(index: int):
        # base case: processed every digit, tempans is one full combination
        if index == len(digits):
            ans.append("".join(tempans))
            return

        letters = phone[digits[index]]
        for ch in letters:
            # CHOOSE this letter for the current digit position
            tempans.append(ch)
            backtrack(index + 1)
            # UNCHOOSE (backtrack)
            tempans.pop()

    backtrack(0)
    return ans


if __name__ == "__main__":
    print(letterCombinations("23"))
    # ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
