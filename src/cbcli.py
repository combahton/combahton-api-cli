import sys
import logging
import click
from modules.antiddos import commands as antiddos
from modules.cloud import commands as cloud
from modules.customer import commands as customer
from modules.config import commands as config
from modules.ipaddr import commands as ipaddr
from modules.ipsubnet import commands as ipsubnet
from tools.config import cfgfile  # pylint: disable=import-error

if getattr(sys, "frozen", False):
    sys.tracebacklimit = 0

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
cli.add_command(ipaddr.ipaddr)
cli.add_command(ipsubnet.ipsubnet)

if __name__ == "__main__":
    cli()
