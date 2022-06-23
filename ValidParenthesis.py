def isValidParenthesis(expression):

    # Write your code here.
    stack = []
 
    # Traversing the Expression
    for char in expression:
        if char in ["(", "{", "["]:
 
            # Push the element in the stack
            stack.append(char)
        else:
 
            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
 
    # Check Empty Stack
    if stack:
        return False
    return True





# Main Code

t = int(input().strip())

for i in range(t):
    str = input().strip()
    ans = isValidParenthesis(str)

    if ans:
        print("Balanced")
        
    else:
        print("Not Balanced")
