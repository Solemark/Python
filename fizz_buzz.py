def fizz_buzz(fizz: int, buzz: int, max: int) -> str:
    output: str = "\b"
    i: int = 1
    while(i <= max):
        if 0 == i % fizz:
            output += "fizz"
        if 0 == i % buzz:
            output += "buzz"
        if "z" != output[len(output)-1]:
            output += str(i)
        output += "\n"
        i += 1
    return output

print(fizz_buzz(3, 5, 20))
