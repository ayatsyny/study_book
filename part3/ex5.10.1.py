

def f(a, *, b):
    """Если вы вообще не хотите поддерживать позиционные аргументы, оставив, тем не менее, возможность, задавать
    чисто именованные, включите в сигнатуру звездочку * саму по себе:"""
    return a, b


print(f(1, b=2))
