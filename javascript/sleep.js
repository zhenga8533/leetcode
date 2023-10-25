/**
 * @param {number} millis
 * @return {Promise}
 */
const sleep = async (millis) => {
    // Runtime: 53 ms (Beats 52%)
    // Memory: 41.5 MB (Beats 65.91%)
  
    await new Promise(resolve => setTimeout(resolve, millis))
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */
 
