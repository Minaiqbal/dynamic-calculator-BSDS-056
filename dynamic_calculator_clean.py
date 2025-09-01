def calc(expr):
    expr = expr.replace("×","*").replace("÷","/")
    stack = []
    num = ""
    for ch in expr:
        if ch.isdigit() or ch==".":
            num += ch
        else:
            if num:
                stack.append(float(num))
                num = ""
            stack.append(ch)
    if num:
        stack.append(float(num))

    i=0
    while i<len(stack):
        if stack[i]=="*" or stack[i]=="/":
            if stack[i]=="*":
                val = stack[i-1]*stack[i+1]
            else:
                val = stack[i-1]/stack[i+1]
            stack[i-1:i+2] = [val]
            i -= 1
        else:
            i+=1

    i=0
    while i<len(stack):
        if stack[i]=="+" or stack[i]=="-":
            if stack[i]=="+":
                val = stack[i-1]+stack[i+1]
            else:
                val = stack[i-1]-stack[i+1]
            stack[i-1:i+2] = [val]
            i -= 1
        else:
            i+=1
    return stack[0]

expr = "1+2×3-4÷2"
print(calc(expr))

