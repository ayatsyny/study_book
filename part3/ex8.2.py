

class Gizmo:
    def __init__(self):
        print(f'Gizmo id {self}')


if __name__ == '__main__':
    x = Gizmo()
    try:
        y = Gizmo() * 10
    except TypeError as e:
        print(e)
    print(dir())
