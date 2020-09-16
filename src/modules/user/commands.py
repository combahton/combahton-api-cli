import click
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

@click.group()
def user():
    """api user module"""
    pass

@click.command()
@click.argument('email')
@click.argument('key')
def login(email, key):
    """Login with your api credentials and save them to config.ini"""
    with open("config.ini", "w") as f:
        if not config.has_section('api'):
            config.add_section('api')
        config.set('api', 'email', email)
        config.set('api', 'key', key)
        config.write(f)
    click.echo("Saved credentials for %s" % email)

@click.command()
def show():
    """Show stored credentials from config.ini"""
    if not config.has_section('api'):
        click.echo("No credentials saved.")
    else:
        click.echo("Logged in as %s with key %s" % (config.get('api', 'email'), config.get('api', 'key')))

@click.command()
def logout():
    """Remove stored credentials from config.ini"""
    if config.has_section('api'):
        with open('config.ini', 'w') as f:
            f.write("")
    else:
        click.echo("There were no credentials stored.") 

user.add_command(login)
user.add_command(show)
user.add_command(logout)