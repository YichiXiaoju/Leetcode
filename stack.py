def isValid(s):
    stack = []
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return not stack

def removeDuplicates(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

def inversePolishNotation(tokens):
    stack = []
    operators = {'+', '-', '*', '/'}
    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  # Use int() to truncate towards zero
    return stack[0]

def dailyTemperatures(temperatures):
    answer = [0] * len(temperatures)
    stack = []

    for right in range(len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[right]:
            previous_day = stack.pop()
            answer[previous_day] = right - previous_day

        stack.append(right)

    return answer

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)

        if not self.min_stack:
            self.min_stack.append(value)
        else:
            self.min_stack.append(
                min(value, self.min_stack[-1])
            )

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

def decodeString(s):
    stack = []
    current_string = ""
    current_number = 0

    for char in s:
        if char.isdigit():
            current_number = current_number * 10 + int(char)

        elif char == "[":
            stack.append((current_string, current_number))
            current_string = ""
            current_number = 0

        elif char == "]":
            previous_string, repeat_number = stack.pop()
            current_string = (
                previous_string
                + repeat_number * current_string
            )

        else:
            current_string += char

    return current_string

