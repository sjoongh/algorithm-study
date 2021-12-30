while(True):
    li = []
    s = input()
    if s == '.':
        break
    for i in s:
        if i == '(' or i == '[':
            li.append(i)

        elif i == ')':
            if len(li) == 0:
                li.append('.')
                break
            elif li[-1] != '(':
                break
            else:
                li.pop()
        elif i == ']':
            if len(li) == 0:
                li.append('.')
                break
            if li[-1] != '[':
                break
            else:
                li.pop()
    if li:
        print("no")
    else:
        print("yes")