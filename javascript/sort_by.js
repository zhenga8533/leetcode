/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    // Runtime: 131 ms (Beats 40.7%)
    // Memory: 56.1 MB (Beats 81.18%)
  
    return arr.sort((a, b) => fn(a) - fn(b));
};
