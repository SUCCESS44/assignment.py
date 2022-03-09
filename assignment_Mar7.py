#!/home/ojokere/Development/python_project/bin/python
import click

@click.command() #creates a basic click application for you
@click.option('--scripting', default ='bash', help='what do you want to call your script')
@click.option('--name', default ='shell', help="How is your script")
def language(name, scripting):
    print(f"{scripting} {name}")

if __name__ == "__main__":
    language()    