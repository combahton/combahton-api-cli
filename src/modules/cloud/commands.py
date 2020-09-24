import logging
import json
from configparser import ConfigParser
import click
from tabulate import tabulate
from tools.api import ApiRequest  # pylint: disable=import-error

cfgfile = ConfigParser()
cfgfile.read("config.ini")

logging.basicConfig(
    level=logging.getLevelName(cfgfile.get("core", "verbose"))
    if cfgfile.has_option("core", "verbose")
    else logging.INFO
)
logger = logging.getLogger(__name__)


api = ApiRequest()


@click.group()
def cloud():
    """cloud server management module"""


@click.command()
@click.argument("contract", type=click.INT)
@click.option("-r", "--raw", is_flag=True, help="Return the raw JSON response")
def view(contract, raw):
    request = api.request(component="kvm", method="server", action="view", id=contract)
    response = json.loads(request.text)
    if raw:
        click.echo(response)
    else:
        if response and response["status"] == "id_unauthenticated":
            logger.error("Access denied: You are not allowed to modify %s", contract)
        else:
            res = []
            for key, val in response.items():
                res.append([key, val])
            click.echo(tabulate(res))


# endregion

cloud.add_command(view)
