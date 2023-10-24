/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    // Runtime: 50 ms (Beats 63.42%_
    // Memory: 41.3 MB (Beats 93.27%)
  
    for (let i = 0; i < arr.length; i++)
        arr[i] = fn(arr[i], i)
        
    return arr
};
