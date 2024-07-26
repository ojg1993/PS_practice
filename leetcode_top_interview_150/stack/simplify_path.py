class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []

        for p in path.split("/"):
            if p not in ["", ".", ".."]:
                res.append(p)
            elif res and p == "..":
                res.pop()

        return "/" + "/".join(res)
