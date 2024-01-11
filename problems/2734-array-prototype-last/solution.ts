declare global {
    interface Array<T> {
        last(): T | -1;
    }
}

Array.prototype.last = function() {
    const len = this.length;
    
    if (len === 0) return -1;
    return this[len-1]; 
};

export {};
