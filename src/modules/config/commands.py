import logging
import click
from tools.config import cfgfile, int_configPath  # pylint: disable=import-error

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

    Write config: cbcli config user.email test@example.tld

    Available keys: user.email, user.key
    """
    if index == "location":
        click.echo(int_configPath)
        return

    namespace, key = index.split(".", 1)
    if (
        (value == "" or value is None)
        and namespace
        and key
        and cfgfile.has_option(namespace, key)
    ):
        click.echo(cfgfile.get(namespace, key))
    else:
        with open(int_configPath, "w") as file:
            if not cfgfile.has_section(namespace):
                cfgfile.add_section(namespace)
            cfgfile.set(namespace, key, value)
            cfgfile.write(file)
