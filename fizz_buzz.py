max: int = 20
min: int = 1
fizz: int = 3
buzz: int = 5
output: str = ""

for x in range(min, max+1):
    output = ""
    if x%fizz==0:
        output += "Fizz"
    if x%buzz==0:
        output += "Buzz"
    if output=="":
        output = x
    print(output)