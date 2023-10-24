/**
 * @param {string} val
 * @return {Object}
 */
var expect = val => {
    // Runtime: 56 ms (Beats 25.26%)
    // Memory: 41.8 MB (Beats 60.78%)
  
    return {
        toBe: v => {
            if (val !== v) throw new Error("Not Equal")
            return true
        },
        notToBe: v => {
            if (val === v) throw new Error("Equal");
            return true
        }
    }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */
