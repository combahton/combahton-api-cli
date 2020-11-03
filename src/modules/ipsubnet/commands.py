import logging
import json
import ipaddress
import click
from tools.api import ApiRequest  # pylint: disable=import-error
from tools.config import cfgfile  # pylint: disable=import-error

logging.basicConfig(
    level=logging.getLevelName(cfgfile.get("core", "verbose"))
    if cfgfile.has_option("core", "verbose")
    else logging.INFO
)
logger = logging.getLogger(__name__)


def confirm_callback(ctx, param, value):
    if not param or not value:
        ctx.abort()


@click.group()
def ipsubnet():
    """ip address management module"""


@click.command()
@click.argument("contract")
@click.argument("target")
@click.option("-r", "--raw", is_flag=True, help="Returns the raw json response")
def nexthop(contract, target_ip, raw):
    try:
        api = ApiRequest()
        target_ip = ipaddress.ip_address(target_ip)
        if not isinstance(target_ip, ipaddress.IPv4Address):
            raise ValueError()

        request = api.request(
            component="ipsubnet",
            method="nexthop",
            action="change",
            contract=contract,
            nexthop=str(target_ip),
        )

        if raw:
            click.echo(request.text)
        else:
            response = json.loads(request.text)
            if response and "status" in response:
                if response["status"] == "id_unauthenticated":
                    logger.error(
                        "Access denied: You are not allowed to modify %s", str(contract)
                    )
                elif response["status"] == "rdns_changed":
                    logger.info("RDNS/PTR changed successfully")
            else:
                logger.error(
                    "An unhandled response was received. Use --raw to see the raw json response."
                )

    except:
        logger.error("An error occured.")
        raise


ipsubnet.add_command(nexthop)
