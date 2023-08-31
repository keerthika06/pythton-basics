secret_word = "Honey"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False

while guess!= secret_word and not(out_of_guess):
    if guess_count < guess_limit:
        guess= input("enter guess")
        guess_count +=1
    else:
        out_of_guess = True

if out_of_guess :
    print("you loose")
else:
    print("you won")

print("*********for***************")
name = ["hi","hello","how","are","you"]
for letter in "name":
    print(letter)
for letter in name:
    print(letter)

print("***********exponent*************")

def raise_to_power(base_num , pow_num):
    result = 1
    for i in range(pow_num):
        result = result * base_num
    return result
print(raise_to_power(8,2))

print("***********List and nested loops*************")

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[3][0])

for row in number_grid :
    print(row)


for row in number_grid:
    for col in row:
        print(col)

print("***********translator**************")

def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translator(input("enter a phrase")))


print("**********try except*********")

try:
    number = int(input("enter a no: "))
    print(number)
except:
    print("invalid input")
