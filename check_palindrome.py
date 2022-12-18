def check_palindrome(input: str) -> bool:
    if isinstance(input, str):
        i: int = (len(input) - 1)
        for c in input:
            if c != input[i]:
                return False
            i -= 1
        return True
    else:
        return False