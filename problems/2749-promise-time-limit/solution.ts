type Fn = (...params: any[]) => Promise<any>;

function timeLimit(fn: Fn, t: number): Fn {
    const timer = new Promise((_, reject) => {
        setTimeout(() => reject("Time Limit Exceeded"), t);
    });

    return async function(...args) {
        return Promise.race([fn(...args), timer]);    
    }
};
