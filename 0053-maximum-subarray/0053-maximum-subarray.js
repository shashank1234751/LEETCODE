var maxSubArray = function(nums) {
    let curr = nums[0];
    let ans = nums[0];

    for (let i = 1; i < nums.length; i++) {
        curr = Math.max(curr + nums[i], nums[i]);
        ans = Math.max(curr, ans);
    }

    return ans;
};