# Practice1
## Back to School
1. Given `phi = 3.1415` and `r = 15`, calculate the value of phi * r<sup>2</sup>.

2. Given `a = 10` and `b = 15`, calculate the value of `c`, such that a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup> holds.

3. Given `phi = 3.1415` and `r = 15`, calculate the value of 4 / 3 * phi * r<sup>3</sup>.

4. Calculate the value of `sin(30°)`.

## Next 5?
For each of the following sequences, complete it by printing the next 5 numbers.

* 2, 4, 6, 8, 10, ...
* 8, 6, 4, 2, 0, ...
* 1, 4, 9, 16, 25, ...
* 1, 1, 2, 3, 5, ...

## GPA Calculator
Create a program that takes a GPA grade as an input, and output the corresponding GPA value.

|Input|Output|
|---|---|
|A+|5.0|
|A|5.0|
|A-|4.5|
|B+|4.0|
|B|3.5|
|B-|3.0|
|C+|2.5|
|C|2.0|
|D+|1.5|
|D|1.0|
|F|0.0|

## Oryh Ohwwhu

`Caesar Cipher` is an encryption technique that replaces each character with another character fixed number of positions down the alphabet. For example, if we are using `Caesar Cipher 3`, then the following encoding holds:
```
a --> d
b --> e
...
z --> c
```
Make a program as a Caesar Cipher decoder. The program takes an encoded message as the input, and output the decoded message. You only need to consider alphabets. Other characters will remain the same both in encoded and decoded messages.

Note: Try to decode the title of this practice. :)


## Pattern Printing
Given the value of integer `n`, print a pattern following the examples below.
### Pattern Printing 1
Note: n >= 1

* n = 3
```
*
**
***
```
* n = 4
```
*
**
***
****
```
* n = 5
```
*
**
***
****
*****
```

### Pattern Printing 2
Note: n >= 1
* n = 3
```
***
**
*
```
* n = 4
```
****
***
**
*
```
* n = 5
```
*****
****
***
**
*
```
### Pattern Printing 3
Note: n >= 1
* n = 3
```
  *
 **
***
```
* n = 4
```
   *
  **
 ***
****
```
* n = 5
```
    *
   **
  ***
 ****
*****
```
### Pattern Printing 4
Note: n >= 1
* n = 2
```
  **
**
   *
*
```
* n = 3
```
   ***
***
    **
**
     *
*
```
* n = 4
```
    ****
****
     ***
***
      **
**
       *
*
```
### Pattern Printing 5
Note: n >= 3
* n = 3
```
*****
*
*****
    *
*****
```
* n = 4
```
*******
*
*
*******
      *
      *
*******
```
### Pattern Printing 6
Note: n >= 1
* n = 3
```
***
 *
 *
***
```
* n = 4
```
****
 **
 **
****
```
* n = 5
```
*****
 ***
  *
  *
 ***
*****
```
### Pattern Printing 7
Note: n >= 3
* n = 3
```
     ***
    *   *
   *     *
  *********
 *         *
*           *
```
* n = 4
```
       ****
      *    *
     *      *
    *        *
   ************
  *            *
 *              *
*                *
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


