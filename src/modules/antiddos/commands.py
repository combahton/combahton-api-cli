import click
import json
import ipaddress
import sys
from api.request import ApiRequest

api = ApiRequest()

@click.group()
def antiddos():
    """antiddos management module"""
    pass


@click.command()
@click.argument('ipv4')
@click.argument('toggle', type=click.BOOL)
def fv3(ipv4, toggle):
    try:
        ipaddr = str(ipaddress.ip_address(ipv4))
        request = api.request(component = "antiddos", method = "layer4", action = "routing", routing = "l4_target", target = ('fv3' if toggle else 'fv3'), ipaddr = ipaddr)
        response = json.loads(request.text)
        if response and response["status"]  == 'routing_changed':
            click.echo("OK")
        else:
            click.echo(response["status"])
    except ValueError:
        click.echo("address/netmask is invalid: %s "  % click.get_os_args()[2])
    except:
        click.echo('Usage: antiddos fv3 127.0.0.1 true')
        raise

antiddos.add_command(fv3)