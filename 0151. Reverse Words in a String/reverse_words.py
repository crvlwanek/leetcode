def reverseWords(s: str) -> str:
    return " ".join(re.findall(r'\b\w+\b', s)[::-1])