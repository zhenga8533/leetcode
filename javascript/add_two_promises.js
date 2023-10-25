/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
const addTwoPromises = async (promise1, promise2) => {
    // Runtime: 55 ms (Beats 78.70%)
    // Memory: 42 MB (Beats 49.95%)
  
    const [res1, res2] = await Promise.all([promise1, promise2])
    return res1 + res2
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */
