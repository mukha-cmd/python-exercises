def is_paired(input_string):
    stack = []
    for ch in input_string:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':              
            if not stack:               
                return False
            top = stack[-1]
            if (top == '(' and ch == ')') or (top == '[' and ch == ']') or (top == '{' and ch == '}'):
                stack.pop()
            else:
                return False
        else:
            continue                    
    return len(stack) == 0
