# _Selection Sort_
## _Steps_
- **What you select?** Select Minimum
- Get the minimum from the array
- Replace the minimum from the first place and the element at first place to the replaced position
- Select minimum & Swap

![selection sort](https://github.com/anupam-kumar-krishnan/A2Z-DSA/assets/69143883/d9511eb7-2af0-4508-ab10-2587e3fb9519)

### _Pseudo Code_

<b>

```cpp
for(i=0;i<=n-2;i++)
{
  minimumIndex=i;
  for(j=i;j<n-1;j++)
  {
    if(arr[j]<arr[minimumIndex]) 
         minimumIndex = j;
  }
  swap(arr[minimumIndex], arr[i])
}
```
</b>

### _Code_

<b>

```cpp
#include <bits/stdc++.h>
using namespace std;
void selection_sort(int arr[], int n) {
  for (int i = 0; i < n - 2; i++) {
    int mini = i;
    for (int j = i; j <= n - 1; j++) {
      if (arr[j] < arr[mini]) {
        mini = j;
      }
    }
    int temp = arr[mini];
    arr[mini] = arr[i];
    arr[i] = temp;
  }
}

int main() {
  int n;
  cin >> n;
  int arr[n];
  for (int i = 0; i < n; i++)
    cin >> arr[i];

  selection_sort(arr, n);

  for (int i = 0; i < n; i++) {
    cout << arr[i] << " ";
  }
  return 0;
}

/*
Input
6
13 46 24 52 20 9

Output
9 13 20 24 46 52
*/
```
</b>

### _Time Complexity of Selection Sort: O(n^2)_

# _Bubble Sort_
- Pushes the _**maximum element**_ to the **_last_** by adjacent swaps

















