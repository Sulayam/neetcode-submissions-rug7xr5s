class Solution:
    def isValid(self, s: str) -> bool:
        stack=["-1"]
        hashmap = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        for i, char in enumerate(s):
            print(f"stack at {i}th iteration:{stack}")
            print(f"stack[-1]:{stack[-1]}")
            # print(f"hashmap[char] {i}th iteration:{hashmap[char]}")
            if char in hashmap and stack[-1]==hashmap[char]:
                stack.pop()
            else:
                stack.append(char)
        flag=False
        if stack[-1]=="-1":
            flag=True
        return flag