/**
 * @return {Function}
 */
const createHelloWorld = () => {
    // Runtime: 43 ms (Beats 88.46%)
    // Memory: 41.8 MB (Beats 29.9%)
    
    return (...args) => {
        return "Hello World"
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */
