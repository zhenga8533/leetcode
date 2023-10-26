/**
 * @param {Function} fn
 * @return {Function}
 */
const once = (fn) => {
  // Runtime: 47 ms (Beats 82.11%)
  // Memory: 41.9 MB (Beats 39.56%)
  
  let unused = true
    
	return (...args) => {
        if (unused) {
            unused = false
            return fn(...args)
        } else return undefined
    }
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
