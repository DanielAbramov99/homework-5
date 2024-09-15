height: float = float(input("enter correct height:"))
while (height > 2.5) or (height < 0.4):
    print("wrong")
    height: float = float(input("enter correct height:"))
else:
    print("correct")

number_input1: int = int(input("enter number"))
number_input2: int = int(input("enter second number:"))
if number_input1 < number_input2:
    for number in range(number_input1, number_input2 + 1, 1):
        print(number, end=" ")
else:
    for number in range(number_input1, number_input2 - 1, -1):
        print(number, end=" ")
print()

pie: float = 3.14
tries = 1
user_attempt: float = float(input("what is pie?:"))
while user_attempt != pie and tries < 3:
    print("wrong")
    tries += 1
    user_attempt: float = float(input("try again, what is pie?:"))
if user_attempt == pie:
    print("correct!")
else:
    print(f"incorrect,the pie is {pie}")

while True:
    num1: int = int(input("enter first number"))
    num2: int = int(input("enter second number"))
    num3: int = int(input("enter third number"))
    num_avg = (num1 + num3) / 2
    if 0 <= num1 <= 10 and 10 <= num2 <= 60 and 60 <= num3 <= 100 and num_avg == num2:
        break
