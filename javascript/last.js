/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
    // Runtime: 44 ms (Beats 85.64%)
    // Memory: 41.9 MB (Beats 32.44%)
  
    return this.length === 0 ? -1 : this[this.length - 1];
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */
