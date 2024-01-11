type Fn = (...params: number[]) => number

function memoize(fn: Fn): Fn {
    const cache = {};

    return function(...args) {
        const key = args.join('#')
        const res = cache[key];
        if (res !== undefined) return res;

        cache[key] = fn(...args);
        return cache[key];
    }
}
