class TimeLimitedCache {
    data: Record<number, {value: number, id: ReturnType<typeof setTimeout>}>;

    constructor() {
        this.data = {};    
    }
    
    set(key: number, value: number, duration: number): boolean {
        const result = this.data[key];

        if (result !== undefined) clearTimeout(result.id);
        this.data[key] = {value, id: setTimeout(() => delete this.data[key], duration)};

        return result !== undefined;
    }
    
    get(key: number): number {
        return this.data[key]?.value ?? -1;
    }
    
    count(): number {
        return Object.keys(this.data).length;
    }
}
