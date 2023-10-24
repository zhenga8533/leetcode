/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = (n) => {
    // Runtime: 54 ms (Beats 31.65%)
    // Memory: 41.5 MB (Beats 83.26%)
  
    return () => {
        return n++
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */
