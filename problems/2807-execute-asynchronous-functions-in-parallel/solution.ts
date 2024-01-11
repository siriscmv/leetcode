type Fn<T> = () => Promise<T>

function promiseAll<T>(functions: Fn<T>[]): Promise<T[]> {
    return new Promise((resolve, reject) => {
        const result = Array(functions.length).fill(undefined);
        let pending = functions.length;

        for (const [i, fn] of functions.entries()) {
            fn().then((res) => {
                result[i] = res;
                if (--pending === 0) resolve(result);
            }).catch(reject);
        }
    });
};
