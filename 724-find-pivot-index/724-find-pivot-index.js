/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    let left = 0
    let right = 0
    for (let i=0; i < nums.length; i++){
        let pivot = i
        if (i > 0){
            left += nums[i-1]
        }
        for (let j=i+1; j < nums.length; j++){
            
            right += nums[j]
            // console.log("left = " + left)
            // console.log("right = " + right)
            
        }
        if (left === right){
            return i
        }
        right = 0
    }
    return -1
};