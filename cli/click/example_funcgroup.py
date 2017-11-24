import click
# this section shows functions that can be called specifically from command line.

@click.group()
def greet():
    pass

@greet.command()
def hello(**kwargs):
    print("hello")
    print()
    pass


@greet.command()
def goodbye(**kwargs):
    print("goodbye")
    pass

if __name__ == '__main__':
    greet()
