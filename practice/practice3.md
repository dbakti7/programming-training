# Practice 3

## How many times the word "Hello" will be printed?
```
for i in range(1, 5, 2):
    print("Hello")
```
<details>
<summary>
Answer
</summary>
2
</details>

```
for i in range(5):
    if (i % 2 == 0):
        print("Hello")
    print("Hello")
```
<details>
<summary>
Answer
</summary>
8
</details>

```
for i in range(5):
    for j in range(i):
        print("Hello")
```
<details>
<summary>
Answer
</summary>
10
</details>

## What will be the output of the following programs?
```
words = ["Greece", "Italy", "Greece", "France", "France", "China", "USA", "Greece"]

counter = 0
for word in words:
    if word == "Greece":
        counter += 1

print(counter)
```
<details>
<summary>
Answer
</summary>
3
</details>

```
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

limit = 7
answer = 0
for number in numbers:
    if number > limit:
        answer += number

print(answer)
```
<details>
<summary>
Answer
</summary>
27
</details>

```
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

limit = 7
answer = 0
counter = 0
for number in numbers:
    if number > limit:
        answer += number
        counter += 1

print(answer / counter)
```
<details>
<summary>
Answer
</summary>
9
</details>

```
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

average = 7.5
answer = 0
for number in numbers:
    if abs(number - average) > 2.0:
        answer += 1

print(answer)
```
<details>
<summary>
Answer
</summary>
6
</details>

```
numbers = [1, 2, 3, 4, 5]
back = len(numbers) - 1
for i in range(len(numbers) // 2):
    temp = numbers[back]
    numbers[back] = numbers[i]
    numbers[i] = temp
    back -= 1

print(numbers)
```
<details>
<summary>
Answer
</summary>
[5, 4, 3, 2, 1]
</details>

## Find one mistake in the following code to get the desired output
```
1 for i in range(10):
2    if (i % 2 == 0):
3        print(i)
```
```
Desired output
1
3
5
7
9
```
<details>
<summary>
Answer
</summary>
On line 2, change to:

if (i % 2 == 1):
</details>

```
1 numbers = [7, 8, 8, 8, 9]
2 total = 0
3 for i in range(len(numbers)):
4     total += i
5 print(total / 5)
```
```
Desired output
8
```
<details>
<summary>
Answer
</summary>
On line 4, change to:

total += numbers[i]

or On line 3, change to:

for i in numbers:
</details>