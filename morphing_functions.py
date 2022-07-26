functions = {
    None: (lambda x, y: x),
    }

def entry(fun):
    functions[fun.__name__] = fun

@entry
def replace(a, b):
    return b
    
@entry
def add(a, b):
    return a+b

@entry       
def katamari(a, b):
    a = str(a)
    for word in b:
        if len(str(word)) < len(a):
            a += str(word)
    return a

@entry
def extend(a, b):
    a.append(b)
    return a
        