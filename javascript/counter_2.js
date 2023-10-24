/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    // Runtime: 63 ms (Beats 30.38%)
    // Memory: 44.1 MB (Beats 88.7%)
  
    const base = init;

    return {
        increment: () => {
            return ++init
        },
        reset: () => {
            return init = base
        },
        decrement: () => {
            return --init
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
