# _Merge Sort_
- Merge Sort takes much better time complexity
- Merge Sort means _**Divide & Merge**_
- Instead of breaking down into 2 parts, play arount with _**Index**_

![merge sort](https://github.com/anupam-kumar-krishnan/A2Z-DSA/assets/69143883/d3086987-8820-4c13-8013-7748dcda5ce5)

## _Pseudo Code_

![merge sort example](https://github.com/anupam-kumar-krishnan/A2Z-DSA/assets/69143883/66008b15-e1d2-4701-afd4-912508f4c6bb)


<b>

```cpp
mergeSort(arr, low, high)
{
  if (low >= high) return;

  mid = (low + high) / 2
  mergeSort(arr, low, mid);
  mergeSort(arr, mid+1, high);
  mergeSort(arr, low, mid, high);
}
```
</b>



