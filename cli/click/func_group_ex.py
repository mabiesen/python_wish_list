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


#@click.command()
#@click.option('--count', default=1, help='Number of greetings.')
#@click.option('--name', prompt='Your name',
#              help='The person to greet.')
#def hello(count, name):
#    """Simple program that greets NAME for a total of COUNT times."""
#    for x in range(count):
#        click.echo('Hello %s!' % name)

#if __name__ == '__main__':
#    hello()
