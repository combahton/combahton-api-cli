import logging
import json
import ipaddress
import click
from tabulate import tabulate
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
def ipaddr():
    """ip address management module"""


@click.command()
@click.argument("ip_addr")
@click.option("-r", "--raw", is_flag=True, help="Returns the raw json response")
def view(ip_addr, raw):
    api_action = "unknown"
    try:
        api = ApiRequest()
        ip_addr = ipaddress.ip_address(ip_addr)
        if isinstance(ip_addr, ipaddress.IPv4Address):
            api_action = "ipv4"
        elif isinstance(ip_addr, ipaddress.IPv6Address):
            api_action = "ipv6"

        request = api.request(
            component="ipaddr", method="view", action=api_action, ipaddr=str(ip_addr)
        )

        if raw:
            click.echo(request.text)
        else:
            response = json.loads(request.text)
            if (
                response
                and "status" in response
                and response["status"] == "id_unauthenticated"
            ):
                logger.error(
                    "Access denied: You are not allowed to modify %s", str(ip_addr)
                )
            else:
                res = []
                for key, val in response.items():
                    res.append([key, val])
                click.echo(tabulate(res))

    except:
        logger.error("An error occured.")
        raise


@click.command()
@click.argument("ip_addr")
@click.argument("reverse_dns")
@click.option("-r", "--raw", is_flag=True, help="Returns the raw json response")
def rdns(ip_addr, reverse_dns, raw):
    api_action = "unknown"
    try:
        api = ApiRequest()
        ip_addr = ipaddress.ip_address(ip_addr)
        if isinstance(ip_addr, ipaddress.IPv4Address):
            api_action = "ipv4"
        elif isinstance(ip_addr, ipaddress.IPv6Address):
            api_action = "ipv6"

        request = api.request(
            component="ipaddr",
            method="rdns",
            action=api_action,
            ipaddr=str(ip_addr),
            ptr=reverse_dns,
        )

        if raw:
            click.echo(request.text)
        else:
            response = json.loads(request.text)
            if response and "status" in response:
                if response["status"] == "id_unauthenticated":
                    logger.error(
                        "Access denied: You are not allowed to modify %s", str(ip_addr)
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


ipaddr.add_command(view)
ipaddr.add_command(rdns)
