import logging
from configparser import ConfigParser
import click

cfgfile = ConfigParser()
cfgfile.read("config.ini")

logging.basicConfig(
    level=logging.getLevelName(cfgfile.get("core", "verbose"))
    if cfgfile.has_option("core", "verbose")
    else logging.INFO
)
logger = logging.getLogger(__name__)


@click.command()
@click.argument("index")
@click.argument("value", default="")
def config(index, value):
    """Configuration Module

    Read from config: cbcli config user.email

    Write to config: cbcli config user.email test@example.com"""
    namespace, key = index.split(".", 1)
    if value == "" and namespace and key and cfgfile.has_option(namespace, key):
        click.echo(cfgfile.get(namespace, key))
    else:
        with open("config.ini", "w") as file:
            if not cfgfile.has_section(namespace):
                cfgfile.add_section(namespace)
            cfgfile.set(namespace, key, value)
            cfgfile.write(file)
