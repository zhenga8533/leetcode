/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    // Runtime: 45 ms (Beats 87.81%)
    // Memory: 42.4 MB (Beats 7.94%)
    
    const filtered = []

    arr.forEach((n, i) => {
        if (fn(n, i))
            filtered.push(n)
    })

    return filtered
};
