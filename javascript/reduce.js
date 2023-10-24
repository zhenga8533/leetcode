/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    // Runtime: 55 ms (Beats 46.81%)
    // Memory: 42.3 MB (Beats 59.7%)
  
    nums.forEach(num => {
        init = fn(init, num)
    })

    return init
};
