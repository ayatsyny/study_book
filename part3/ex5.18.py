import imp
import inspect


if __name__ == '__main__':
    tag = imp.load_source('tag', 'ex5.10.py')
    sig = inspect.signature(tag.tag)
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
    bound_args = sig.bind(**my_tag)
    print(bound_args)
    for name, value in bound_args.arguments.items():
        print(name, '=', value)
    print(my_tag)
    del my_tag['name']
    print('remove "name" my_tag')
    print(my_tag)
    bound_args = sig.bind(**my_tag)  # error normal
    print(bound_args)
