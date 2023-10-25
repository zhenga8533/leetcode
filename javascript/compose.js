/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
  // Runtime: 52 ms (Beats 96.29%)
  // Memory: 42.8 MB (Beats 94.49%)
    
	return function(x) {
        for (let i = functions.length - 1; i >= 0; i--)
            x = functions[i](x)
        return x
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */
