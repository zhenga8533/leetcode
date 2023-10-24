/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    // Runtime: 47 ms (Beats 91.35%)
    // Memory: 44.7 MB (Beats 30.89%)
  
    const chunky = []
    let i = 0

    while (i < arr.length)
        chunky.push(arr.slice(i, i += size))

    return chunky
};
