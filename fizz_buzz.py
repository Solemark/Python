max = 20
min = 1
fizz = 3
buzz = 5
output = ""

for x in range(min, max+1):
    output = ""
    if x%fizz==0:
        output += "Fizz"
    if x%buzz==0:
        output += "Buzz"
    if output=="":
        output = x
    print(output)