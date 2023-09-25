function findTheDifference(s: string, t: string): string {
    let initial = s.split('');
    const final = t.split('');

    for (const letter of final) {
        const index = initial.indexOf(letter);
        if (index !== -1) {
            initial.splice(index, 1);
        } else {
            return letter;
        }
    }
};
