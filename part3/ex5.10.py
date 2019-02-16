

def tag(name, *content, cls=None, **attrs):
    """Generate one or some HTML-tags"""

    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attrs_str = ''.join(f' {attr}="{value}"' for attr, value in sorted(attrs.items()))
    else:
        attrs_str = ''
    if content:
        return '\n'.join(f'<{name}{attrs_str}>{c}</{name}>' for c in content)
    else:
        return f'<{name}{attrs_str} />'


if __name__ == '__main__':
    print(tag('br'))                                    # 1
    print(tag('p', 'hello'))                            # 2
    print(tag('p', 'hello', 'world'))
    print(tag('p', 'hello', id=33))                     # 3
    print(tag('p', 'hello', 'world', cls='sidebar'))    # 4
    print(tag(content='testing', name='img'))           # 5
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
    print(tag(**my_tag))

