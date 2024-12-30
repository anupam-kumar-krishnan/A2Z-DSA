1. Move Zeros

   ```cpp
   class Solution {
public:
    void moveZeroes(vector<int>& nums) {

        vector<int> temp;

        for(int i=0;i<nums.size();i++) {
            if(nums[i] != 0)
            {
                 temp.push_back(nums[i]);
            }
        }

        int nz=temp.size();
        for(int i=0;i<nz;i++){
            nums[i] = temp[i];
        }

        for(int i=nz;i<nums.size();i++){
            nums[i] = 0;
        }

        for(int i=0;i<nums.size();i++){
           cout<<nums[i]<<",";
        }
    }
};
   ```
