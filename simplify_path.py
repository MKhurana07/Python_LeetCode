def simplify_path(path):
    path = [p for p in path.split("/") if p != "." or p!="" ]
    stack = []
    for n in path:
        if n == "..":
            if len(stack) >0:
                stack.pop()
        else:
            stack.append(n)
    return "/".join(stack)


print(simplify_path("/C:/../Documents/"))
