import imp
from inspect import signature

if __name__ == '__main__':
    clip = imp.load_source('clip', 'ex5.15.py')
    sig = signature(clip.clip)
    print(dir(sig))
    print(sig)
    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default)
