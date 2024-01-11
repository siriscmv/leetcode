type Callback = (...args: any[]) => any;
type Subscription = {
    unsubscribe: () => void
}

class EventEmitter {
    subscribers: Record<string, Callback[]>

    constructor() {
        this.subscribers = {};
    }

    subscribe(eventName: string, callback: Callback): Subscription {
        if (this.subscribers[eventName] === undefined) this.subscribers[eventName] = [];
        const index = this.subscribers[eventName].push(callback) - 1;

        return {
            unsubscribe: () => {
                this.subscribers[eventName][index] = null;
            }
        };
    }
    
    emit(eventName: string, args: any[] = []): any[] {
        const ans = [];
        if (this.subscribers[eventName] === undefined) return ans;

        for (const cb of this.subscribers[eventName]) {
            if (cb !== null) ans.push(cb(...args))
        }
        
        return ans;
    }
}
