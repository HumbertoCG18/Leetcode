class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        left = right = 0
        q = [(left, right, '')]
        while q:
            left, right, s = q.pop()
            if len(s) == 2 * n:
                result.append(s)
            if left < n:
                q.append((left + 1, right, s + '('))
            if right < left:
                q.append((left, right + 1, s + ')'))
        return result