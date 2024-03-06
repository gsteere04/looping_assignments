def char_count_while(s: str, c: str) -> int:
    count = 0
    char_counter = 0
    while char_counter < len(s):
        if s[char_counter] == c:
            count += 1
        char_counter += 1
    return count

def char_count_for(s: str, target_char: str) -> int:
    count = 0
    for char_counter in range(len(s)):
        if s[char_counter] == target_char:
            count += 1
    return count

def char_count_foreach(s: str, target_char: str) -> int:
    count = 0

    for char in s:
        if char == target_char:
            count += 1
    return count
    