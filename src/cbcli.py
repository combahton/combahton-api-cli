import sys
import logging
from configparser import ConfigParser
import click
from modules.antiddos import commands as antiddos
from modules.cloud import commands as cloud
from modules.customer import commands as customer
from modules.config import commands as config

if getattr(sys, "frozen", False):
    sys.tracebacklimit = 0

cfgfile = ConfigParser()
cfgfile.read("config.ini")

logging.basicConfig(
    level=logging.getLevelName(cfgfile.get("core", "verbose"))
    if cfgfile.has_option("core", "verbose")
    else logging.INFO
)
logger = logging.getLogger(__name__)


@click.group()
def cli():
    """Simple CLI Interface to interact with the combahton API"""


cli.add_command(antiddos.antiddos)
cli.add_command(config.config)
cli.add_command(customer.customer)
cli.add_command(cloud.cloud)

if __name__ == "__main__":
    cli()
