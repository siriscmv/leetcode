declare global {
    interface Array<T> {
        groupBy(fn: (item: T) => string): Record<string, T[]>
    }
}

Array.prototype.groupBy = function<T>(fn: (item: T) => string) {
    const ans: Record<string, T[]> = {};
    
    for (const element of this) {
        const key = fn(element);
        if (ans[key] === undefined) ans[key] = [];
        ans[key].push(element);
    }

    return ans;
}
