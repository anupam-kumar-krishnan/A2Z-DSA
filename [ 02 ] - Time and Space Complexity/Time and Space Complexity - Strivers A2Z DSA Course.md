# _Time Complexity_

> _**Time Complexity != Time Taken**_

- _**Time Complexity:**_ Rate at which _**time taken**_ increases with respect to the _**input size**_ rather.

![tc](https://user-images.githubusercontent.com/91872149/210204496-2692d57c-0dd0-4e8f-a331-bd1d66792889.png)

## _Time Complexity is calculated in terms of `Big O Notation`_
- _TC:_ _**Big - Oh Notation**_ -> O( )
- Inside the bracket, time taken is written


### _TC of below Code:_

<b>

```cpp
for(i=1 ; i<=5 ; i++){
    cout<<"Raj";
}

// for loop is running for 5 times
// increment -> check -> print
// for every time(5 Times), it is operating thrice(3)
// i.e. 5*3=15 

for(i=1 ; i<=N ; i++){
    cout<<"Raj";
}
// Here, for every time(N times), it is operating 3 times
// So, O(N x 3) i.e. O(3N)
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

- **_Time Complexity_**, Always compute Time Complexity in Worst Case Scenario
- **_Avoid Constants_**
- **_Avoid Lower Values_**

## _3 Cases of Time Complexity_

![All 3 cases](https://user-images.githubusercontent.com/91872149/210206118-0cf9b3e3-abe7-40d7-b94b-e26eba5812e4.png)

## _Why we compute in the Worst Case_
- If you are building a system, will you build it for 1 Person or for 1 Million People
- You always want the system to Scale up. You will say 1 Million People becuase you always think of the worst that can happen

## _Notations_
![Notations](https://user-images.githubusercontent.com/91872149/210206963-13b21b89-42c3-4f02-bcc8-3091c8d68223.png)

### _Find the Time Complexity of the below code_

<b>

```cpp
for(int i=0;i<N;i++)
{
  for(int j=0;j<N;j++)
  {
   |----------- -> Block of code, Constant Time
  }
}

// i=0 [j=0,1,2,3,....N-1]
// i=1 [j=0,1,2,3,.....N-1]
// i=N-1[j=0,..........N]
// O(N^2)
```

```cpp
for(i=0;i<N;i++)
{
  for(j=0;j<=i;j++)
  {
   code
  }
}
// i=0 [j=0]
// i=1 [j=0,1]
// i=2 [j=0,1,2]
// i=n-1 [n=0,1,2,...,n-1]
// 1+2+3+4+...n = sum of n natural numbers
// (Nx(N+1))/2 = (N)^2/2 + N/2 = N^2/2 (Ignore N/2) =N^2 (Ignore 1/2)
```
</b>



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
