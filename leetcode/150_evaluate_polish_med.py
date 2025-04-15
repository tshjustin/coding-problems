class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        if number: 
            push to stack 


        if operand: 
            evaluate the last 2, then push to the stack 


        """

        operands = ["+", "-", "/", "*"]
        stack = []

        for token in tokens: 

            if token in operands: 
                element_1 = int(stack.pop())
                element_2 = int(stack.pop())

                if token == "+":
                    stack.append(element_1 + element_2)

                elif token == "-":
                    stack.append(element_2 - element_1)

                elif token == "*":
                    stack.append(element_1 * element_2)

                else: 
                    stack.append(int(element_2 / element_1)) # // => floor division to lower bound, could be float / not float. / => normal div, could be float / not float
            
            else: 
                stack.append(int(token))

        return stack[0]

        