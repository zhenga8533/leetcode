/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    // Runtime: 34 ms (Beats 99.73%)
    // Memory: 42.7 MB (Beats 53.2%)
  
    return Object.keys(obj).length === 0
};
