# Practice 2

## Note
If you encounter an infinite loop (your program is stucked inside a loop forever) and you can't type anything on your terminal (or command prompt), don't panic!
Simply close the terminal, try to find the bug, fix it and start over. If you are stucked in the loop again, repeat the process until the bug is fixed! :)

Some of the problems presented here might trap you into this magical bug, so stay sharp and happy coding! ;)

## Syntax Corner
The following Python syntax might help you:
### Reading A Line Containing Integers
Assume you want to read a line containing integers separated by spaces. You can read them into a list of integers as follow:
```
# Sample Input: 1 5 15 10 2
inp = input() # inp is the input string now
inp = inp.split(" ") # inp is a list of string now
for i in range len(inp):
    inp[i] = int(inp[i]) # cast each of them to integer
```

### Initializing List
If you want to create a list containing n elements with certain values initialized into them, you can do it as follow:
```
# let's say we want list of 10 zeros
values = [0 for i in range(10)]
```

## How Many Colas?
Pentium loves a drink called `Cola`. Just recently, there is a promotion by Cola, whereby for each 3 bottle caps, you can exchange them for one bottle of free Cola. 

For example, if he buys 6 colas, he will have 6 bottle caps to be exchanged for additional 2 colas, giving him 8 bottles in total. However, if he buys 9 colas, he will end up with 13 colas. Pentium is good at counting, so he will always look for maximum number of colas he could get.

Pentium has enough money to buy `n` bottles of Cola, can you find out how many maximum colas he will get?

Make a program that takes an integer, `n`, as the input, where `n` denotes the number of colas Pentium buys initially, and `1 <= n <= 1000`. The program should output an integer that tells us how many colas Pentium will get eventually.

|Sample Input|Sample output|
|---|---|
|2|2|
|3|4|
|9|13|
|30|44|
|31|46|
|32|47|
|33|49|
|1000|1499|

<details>
<summary>
Hint1
</summary>
There are 4 components in loop:

1. Value initializations
2. Termination condition
3. Values Update
4. Loop Body

Try to figure out the pseudocode for each of them. (Step 3 and 4 sometimes can be formulated together)
</details>

<details>
<summary>
Hint2
</summary>
Let's start with step 1, what values you need to keep track throughout the loop?

1. We need to keep track of the total number of colas that we can get, this will be the final answer at the end of the program, let's called this variable `bottle`.
2. We need to keep track of how many bottle caps we hold at each iteration, let's call this `caps`.

Next, try to determine the values initialization for these 2 variables. Take note that how you initialize the values might affect the logic in your loop body, and vice versa.
</details>

<details>
<summary>
Hint3
</summary>
Next, let's figure out the termination condition. As long as we still have 3 or more `caps`, we are still able to exchange them for new bottles, hence we only stop the loop when `caps` is smaller than 3. Try to convert it into `while` loop syntax. Remember that termination condition is the exact opposite of conditional check in loop syntax.

```
while(conditional_check_is_true):
    Loop Body
```
</details>

<details>
<summary>
Hint4
</summary>
For the loop body, the following logics are needed:

1. Update total number of bottles we have accumulated so far. Remember, for each 3 caps, we get one new bottle.

2. Update number of caps that we have. We exchange as many caps as possible (We need to subtract from `caps` by the biggest multiple of 3 that is smaller than or equal to previous value of `caps`). After that, we also get one new cap for each new bottle that we get, add this into `caps`.

By following this logic, at each iteration, we only add new bottles obtained from exchanging bottle caps. It means our loop doesn't take initial bottles into consideration. Hence, it must be taken care of at the values initialization.

Try to convert this hint into the actual code.
</details>

<details>
<summary>
Hint5
</summary>
The loop body from previous hint can be captured as follow:

```
bottle = bottle + caps // 3
caps = caps - (caps // 3) * 3 + (caps // 3)
```

Notice that `(caps // 3) * 3` is one way to get the biggest multiple of 3 that is smaller than or equal to `caps`.

Biggest multiple of 3: `3 * multiplier <= caps`. `caps // 3` is to find out this `multiplier` value.

The other term `+ (caps // 3)` is added because we get one new cap from the bottle we exchange.

In addition, the values initialization are as follow:
```
# n is the user input
bottles = n
caps = n
```
</details>

## Climb, Panda! Climb!
Panda loves climbing bamboo trees. Every one move, panda can climb up 30 cm. But because the trees are slippery, everytime panda climb up, he will slip down for 20 cm. The good news is, once panda reached the top of the tree, he could get a good grip and will not slip down after that. Given the height of the bamboo tree, help panda to determine how many moves he need to reach the top of the panda tree!

Make a program that takes an integer, `n`, as the input. `n` denotes the height of the bamboo tree in centimetres. `30 <= n <= 1000`. Output an integer that tells us how many moves are needed by panda to reach the top of the tree.

|Sample Input|Sample output|
|---|---|
|30|1|
|40|2|
|42|3|
|100|8|
|101|9|
|500|48|
|1000|98|

<details>
<summary>
Hint1
</summary>
There are 4 components in loop:

1. Value initializations
2. Termination condition
3. Values Update
4. Loop Body

Try to figure out the pseudocode for each of them. (Step 3 and 4 sometimes can be formulated together)
</details>

<details>
<summary>
Hint2
</summary>
Let's start with step 1, what values you need to keep track throughout the loop?

Essentially, we only need to keep track of how high the panda has climbed so far. We have `n` as the input, and we can have another variable, `height`, to keep track of panda's progress.

Another possible implementation is to simply use `n` to keep track of pandas progress: look at `n` as how much left should be climbed by panda.

In addition, we also need to keep track of how many moves have been performed by Panda, let's call it `moves`.
</details>

<details>
<summary>
Hint3</summary>
The termination condition is when pandas have reached the top of the tree. Try to translate it into actual code, depending on whether you use additional `height` variable, the actual code will differ.

Remember that termination condition is the exact opposite of conditional check in loop syntax.

```
while(conditional_check_is_true):
    Loop Body
```
</details>

<details>
<summary>
Hint4</summary>
For loop body, there are only 3 operations:

1. Panda climbs up 30 cm
2. Panda slips down 20 cm
3. Increment `moves` by one

If you use additional `height` variable, `climbs up 30 cm` will translate into `height + 30`, else it will translate into `n - 30`. And vice versa for `slips down`.
</details>

<details>
<summary>
Hint5
</summary>
The catch is where to check for termination condition. If we only check for termination at the beginning, we might get more `moves` then needed. Remember, once panda reached the top, he won't slip down anymore. It means:

```
Climb up 30 cm
Increment moves
If panda has reached the top:
    Break the loop
Slip down 20 cm
```
</details>

## Potter
Harry is practicing with his flying broom for his next tournament. Today, he wants a special training. He asked Hermione to magically create pillars in a straight line. The pillars have the height of a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>. Harry will start from altitude 1 and will fly in a straight line towards these pillars. Every time he is approaching a pillar that is higher than or equal to his current altitude (let's say the pillar height is `x`), he will increase his altitude to `x + 1`.

Meanwhile, Ron is learning programming. He is watching Harry's training and wondering how many times Harry has to increase his altitude. Help Ron to solve this problem!

The input will be integers separated by spaces. The first integer is `n`, denoting the number of pillars. The next n integers are denoting the height of the pillars in sequence from the first pillar to the last. You can assume that `1 <= n <= 100` and the height of each pillar is more than 0 and no more than 100.

Output one integer denoting how many times Harry has to increase his elevation.

|Sample Input|Sample output|
|---|---|
|3 1 2 3|3|
|5 1 2 3 4 5|5|
|5 1 1 1 1 1|1|
|5 5 10 5 3 12|3|
|5 5 10 5 10 12|4|
|1 1|1|
|10 1 2 1 2 2 5 2 5 10 15|5|

<details>
<summary>
Hint1
</summary>
There are 4 components in loop:

1. Value initializations
2. Termination condition
3. Values Update
4. Loop Body

Try to figure out the pseudocode for each of them. (Step 3 and 4 sometimes can be formulated together)
</details>

<details>
<summary>
Hint2
</summary>
Throughout the loop body, we only to keep track of 2 values:

1. Harry's current altitude
2. How many times Harry has increased his altitude
</details>

<details>
<summary>
Hint3
</summary>
The termination condition is simply when we reached the final pillar. Loop over the pillars one by one.
</details>

<details>
<summary>
Hint4
</summary>
For the loop body, for each pillar: check if you need to increase current altitude (which also implies updating the number of times Harry increasing his altitude).
</details>

## Coin Change
Po Land is a country that only uses coins. They have 4 type of coins with the values of 8, 4, 2 and 1. Lala is a merchant at Po Land, often times she needs to gives the change to her customers. To be efficient, she always wants to give the change with fewest number of coins possible. Help her to find out what is the minimum number of coins she has to give for each change amount.

Make a program that takes an integer, `n`, as the input. `n` denotes the amount of change Lala needs to give. Output an integer that denotes the minimum number of coins Lala needs to give. Note that `1 <= n <= 1000`.

|Sample Input|Sample output|
|---|---|
|3|2|
|8|1|
|10|2|
|11|3|
|15|4|
|22|4|
|26|4|
|110|15|

<details>
<summary>
Hint1
</summary>
Consider the coins from the highest value to the lowest values: 8, 4, 2, 1. For each of them, try to use as many coins as possible before moving to the next coin.

In other words, given `8 * a + 4 * b + 2 * c + 1 * d = n`, we try to maximize a, then maximize b, maximize c, and finally maximize d. Note that a, b, c, and d can be 0.

Try to convert this into the actual code.
</details>

<details>
<summary>
Hint2
</summary>
If you are using Python and having difficulty in finding out the implementation details, use a list containing the values of `[8, 4, 2, 1]`. Then simply loops over each of them as the coin value. Also remember the 4 steps in forming loop: values initialization, termination condition, values update and loop body. For this problem, `for` loop might be more intuitive, but `while` loop is also possible.

</details>

## Lights, On!
Landon just moves into a new mansion. The mansion is so big that it has 100 rooms (he numbers them from 1 to 100). Because he is bored, he invents a game with his friend. First, they turn off the lights in every room. Then they choose `n` integers, a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>. For each a<sub>i</sub>, they will toggle the light switch in room a<sub>i</sub>, a<sub>i</sub> * 2, a<sub>i</sub> * 3, and so on.

For example, assume the numbers chosen are 2, 3, and 5. First, Landon will switch on lights in room 2, 4, 6, ..., 100 (Remember, initially all lights are off, so toggling the switch will turn the light on). Next, for room 3, 6, 9, ..., 99, Landon will switch on the light if it was off before, and vice versa, switch off the light if it was on before. Lastly, he will repeat the process for room 5, 10, 15, ..., 100.

Now, Landon is wondering how many lights are on at the end of this process. Help him to find this out! He is too tired after all of these, anyway.

The input will be integers separated by spaces. The first integer is `n`, denoting how many numbers are chosen. The next n integers are denoting the numbers chosen by Landon and his friend. You can assume that `1 < n < 10` and `1 <= number_chosen <= 100`.

Output an integer, denoting the number of lights that are on at the end of the whole process.

|Sample Input|Sample output|
|---|---|
|1 1|100|
|1 2|50|
|3 2 3 5|51|
|5 2 3 5 7 11|46|
|5 11 22 33 44 55|5|
|7 1 7 23 57 79 90 95|78|
|10 2 11 35 47 61 88 12 99 15 100|45|

<details>
<summary>
Hint1
</summary>
To be added.. :)
</details>