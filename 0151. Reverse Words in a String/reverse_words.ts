function reverseWords(s: string): string {
    return [...s.matchAll(/\b\w+\b/g)].map(match => match[0]).reverse().join(" ")
};