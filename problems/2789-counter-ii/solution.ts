type Counter = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
}

function createCounter(init: number): Counter {
    const base = init;
    let current = base;
    
    return {
        increment: () => ++current,
        decrement: () => --current,
        reset: () => current = base,
    }
};
