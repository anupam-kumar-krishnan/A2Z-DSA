1. Largest Element in Array

```cpp
class Solution {
  public:
    int largest(vector<int> &arr) {
        // code here
        int max=arr[0];
        
        for(int i=0;i<arr.size();i++){
            if(max<arr[i]){
                max=arr[i];
            }
        }
        
        return max;
    }
};
```

2. Second Largest Element in an Array

```cpp
class Solution {
  public:
   int getSecondLargest(vector<int> &arr) {
        // Code Here
        int lg=arr[0], slg=-1;
        for(int i=0;i<arr.size();i++){
            if(lg<arr[i]){
                slg=lg;
                lg=arr[i];
            }
            
            else if(arr[i] < lg && arr[i] > slg){
                slg=arr[i];
            }
        }
        return slg;
    }
    
};
```

3. Check if Array is Sorted

```cpp
bool check(vector<int>& nums) {
        int cnt=0,n=nums.size();
        for(int i=0;i<n-1;i++){
            if(nums[i]>nums[i+1])
               cnt++;
        }      
            if(nums[n-1] > nums[0]){
                cnt++;
            }    
            
        return cnt <= 1;
    }
```

4. Remove Duplicates from a Sorted Array

```cpp
int removeDuplicates(int arr[], int n) {
  set < int > set;
  for (int i = 0; i < n; i++) {
    set.insert(arr[i]);
  }
  int k = set.size();
  int j = 0;
  for (int x: set) {
    arr[j++] = x;
  }
  return k;
}
```

5. Left Rotate Array

```cpp
void solve(int arr[], int n) {
  int temp[n];
  for (int i = 1; i < n; i++) {
    temp[i - 1] = arr[i];
  }
  temp[n - 1] = arr[0];
  for (int i = 0; i < n; i++) {
    cout << temp[i] << " ";
  }
  cout << endl;
}
```   
