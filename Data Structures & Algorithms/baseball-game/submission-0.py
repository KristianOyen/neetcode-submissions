class Solution:
    def calPoints(self, operations: List[str]) -> int:
        bb = []
        for op in operations: 
            if op == "+":
                bb.append(bb[-1] + bb[-2])
            elif op == "D":
                bb.append(bb[-1] * 2)
            elif op == "C":
                bb.pop()   
            else:
                bb.append(int(op))

        return sum(bb)