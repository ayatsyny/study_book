import bobo


@bobo.query('/')
def hello(person):
    return f'Hello {person}!'

# run bobo -f [file name] ex5.12.py
# curl -i http://localhost:8080/?person=Jim