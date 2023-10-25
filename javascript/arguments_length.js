/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
const argumentsLength = (...args) => {
  // Runtime: 47 ms (Beats 78.29%)
  // Memory: 41.7 MB (Beats 63.81%)
  
	return args.length
};

/**
 * argumentsLength(1, 2, 3); // 3
 */
