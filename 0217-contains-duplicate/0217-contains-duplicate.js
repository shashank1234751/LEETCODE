/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let seen=new Map()
    for(let i=0;i<nums.length;i++){
        if(seen.has(nums[i])){
            return true
        }
        seen.set(nums[i],i)
    }
    return false
};