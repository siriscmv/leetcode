type Fn = (...params: number[]) => number

function memoize(fn: Fn): Fn {
    const cache = {};
    return function(...args) {
        const key = args.join('|')
        const res = cache[key];
        if (res !== undefined) return res;

        const accRes = fn(...args);
        cache[key] = accRes;
        return accRes;
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */
