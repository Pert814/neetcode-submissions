class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Reverse Polish Notation => 把運算子放在數字後面，完全不需要括號與優先順序
        # 越後面出現的數字越外層 要先算 => 後進先出 => stack
        # 遇到運算子 pop兩個最上層運算再push進去
        stack = []
        for s in tokens:
            if s == "+":
                top1 = stack.pop()
                top2 = stack.pop()
                stack.append(top2 + top1)
            elif s == "-":
                top1 = stack.pop()
                top2 = stack.pop()
                stack.append(top2 - top1)
            elif s == "*":
                top1 = stack.pop()
                top2 = stack.pop()
                stack.append(top2 * top1)
            elif s == "/":
                top1 = stack.pop()
                top2 = stack.pop()
                stack.append(int(top2 / top1)) #float => int
            else:
                stack.append(int(s))# string => int
        return stack[-1]