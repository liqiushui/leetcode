// 912. 排序数组

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function(nums) {
    return nums.sort(function(a, b){return a - b});
};