import click
import sys
import os

from modules.antiddos import commands as antiddos
from modules.cloud import commands as cloud
from modules.customer import commands as customer
from modules.user import commands as user

@click.group()
def cli():
    """Simple CLI Interface to interact with the combahton API"""
    pass


cli.add_command(antiddos.antiddos)
cli.add_command(user.user)
cli.add_command(customer.customer)
cli.add_command(cloud.cloud)

if __name__ == '__main__':
    cli()