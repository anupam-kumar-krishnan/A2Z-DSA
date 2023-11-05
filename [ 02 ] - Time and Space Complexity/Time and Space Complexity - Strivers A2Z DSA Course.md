# _Time Complexity_



> _**Time Complexity != Time Taken**_

- Rate at which time taken increases with respect to the input size rather.

![tc](https://user-images.githubusercontent.com/91872149/210204496-2692d57c-0dd0-4e8f-a331-bd1d66792889.png)


> TC : Big - Oh Notation -> O()

### _Note:_

In the bracket the time take in written
<b>

```cpp
for(i=1 ; i<=5 ; i++){
    cout<<"Raj";
}
```
</b>

## _Steps:_

1. Assigning
2. Comparision
3. Printing
4. Comparision
5. Printing
6. Comparision<br>

**_Note:_** _Stops(6 Steps in total)_

- Note: This is not the Best Practise

## _Best Practises_

- Time Complexity, Worst Case Scenario
- Avoid Constants
- Avoid Lower Values

## _3 Cases of Time Complexity_

![All 3 cases](https://user-images.githubusercontent.com/91872149/210206118-0cf9b3e3-abe7-40d7-b94b-e26eba5812e4.png)

## _Notations_
![Notations](https://user-images.githubusercontent.com/91872149/210206963-13b21b89-42c3-4f02-bcc8-3091c8d68223.png)

## _Space Complexity_
![space complexity](https://user-images.githubusercontent.com/91872149/210208090-090a84b1-0fd8-42dc-bba0-15b188bfa7ee.png)

_**Example**_
![example](https://user-images.githubusercontent.com/91872149/210208684-b208f313-bc9d-4fa8-97d8-a4cb28daf8f0.png)
Here Space Complexity: O(3)

As 3 variables have been used in total

_**Another Example**_ <br>
If we are talking, <br>
int a[N];     i.e. Space Complexity: O[N] - it is taking spaces to store element of the array

<b>

```txt
Imagine, input is a and b
b = a + b
This is wrong, manipulating the data input is wrong
```
</b>

Most of the server,  1s ~~ 10^8 executes per operation


## _Note:_
- Never do anything to the input
