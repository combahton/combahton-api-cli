import click

@click.group()
def antiddos():
    """antiddos management module"""
    pass


@click.command()
@click.argument('toggle')
def fv3(toggle):
    if toggle == True or toggle == "enable":
        click.echo(toggle)

antiddos.add_command(fv3)