class Solution:
    def isValid(self, s: str) -> bool:
        stack=["-1"]
        hashmap = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        for char in s:
            if char in hashmap and stack[-1]==hashmap[char]:
                stack.pop()
            else:
                stack.append(char)
        flag=False
        if stack[-1]=="-1":
            flag=True
        return flag