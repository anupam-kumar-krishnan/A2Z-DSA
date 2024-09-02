# Largest Element in Array
**Brute Force Approach:**
- Sort the array
- Return the last element
- Time Complexity: O(NlogN)

**Optimized Approach:**
- Take max as the first element
- Compare it with next element
- Change the value of max if next is greater
- Time Complexity: O(logN)

# Second Largest Element in Array
**Brute Force Approach:**
- O(2N) = O(N)
- One from the first pass, second from another

```cpp
    int print2largest(vector<int> &arr) {
       int n=arr.size(),lg=arr[0];

       for (int i=0;i<n;i++){
           if(arr[i] > lg)
           lg=arr[i];
       }

       int slg=-1;

       for(int i=0;i<n;i++)
       {
           if(arr[i]>slg && arr[i]!=lg)
           slg=arr[i];
       }
       
       return slg;  
    }
```

**Optimized Approach:**
- O(N)

```cpp
class Solution {
  public:
    // Function returns the second
    // largest elements
    int secondLargest(vector<int> &arr, int n){
        int largest = arr[0];
        int slargest = -1;
        for(int i=0;i<n;i++){
            if(arr[i] > largest){
                slargest = largest;
                largest = arr[i];
            }
            else if(arr[i] < largest && arr[i] > slargest){
                slargest = arr[i];
            }
        }
        return slargest;
    }
    
    int secondSmallest(vector<int> arr, int n){
        int smallest = arr[0];
        int ssmallest = INT_MAX;
        for(int i=1;i<n;i++){
            if(arr[i]< smallest){
                ssmallest = smallest;
                smallest = arr[i];
            }
            else if(arr[i]!=smallest && arr[i]<ssmallest){
             ssmallest = arr[i];
            }
        }
        return ssmallest;
    }
    
    
    int print2largest(vector<int> &arr) {
        // Code Here
        int n=arr.size();
        int slargest=secondLargest(arr,n);
        int ssmallest = secondSmallest(arr, n);
        return slargest;
    }
};
```

# Check if an Array is Sorted or NOT
- Time Complexity: O(N)

```cpp
bool check(vector<int>& nums) {
        int n=nums.size();
        
        for(int i=1;i<n;i++) {
            if(nums[i] >= nums[i-1]) {
            }
            else {
                return false;
            }
        }
   return true;
}
```

# Remove Duplicates from Sorted Array

```cpp
int removeDuplicates(vector<int>& nums) {
        int i=0;
        for(int j=1;j<nums.size();j++)
        {
            if(nums[i] != nums[j])
            {
              nums[i+1] = nums[j];
              i++;
            }
        }
   return i+1;
}
```

# Left Rotate Array By One

```cpp
vector<int> rotateArray(vector<int>& arr, int n) {
    int temp=arr[0];

    for(int i=1;i<n;i++){
        arr[i-1] = arr[i];
    }
    arr[n-1] = temp;
    return arr;
}
```

# Left rotate the array by D places
- not working properly

```cpp
void rotate(vector<int>& nums, int k) {
        int n=nums.size();
        k = k % n;

        int temp[k];
        for(int i = 0; i < k; i++){
            temp[i] = nums[i];
        }

        for(int i = k; i < n; i++){
            nums[i-k] = nums[i];
        }

        for(int i = n - k; i < n; i++){
            nums[i] = temp[i - ( n - k )];
        }

        for(int i=0;i<k;i++){
            temp.push_back(nums[i]);
        }
    }
```
- _**Working**_

```cpp
void rotate(vector<int>& nums, int k) {
      int n  = nums.size();
      k = k%n;

      reverse(nums.begin(),nums.end());
      reverse(nums.begin(),nums.begin() + k);
      reverse(nums.begin() + k, nums.end());  
}
```



