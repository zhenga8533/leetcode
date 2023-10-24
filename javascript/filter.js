/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    // Runtime: 35 ms (Beats 99.67%)
    // Memory: 41.9 MB (Beats 55.51%)
  
    return arr.filter(fn)
};
