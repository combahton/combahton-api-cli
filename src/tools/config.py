import pathlib
import os
import sys
from configparser import ConfigParser

# defaultConfigPath = pathlib.Path.joinpath(
# pathlib.Path(__file__).parent.absolute(), "config.ini"
# )

defaultConfigPath = pathlib.Path.joinpath(
    pathlib.Path(os.path.abspath(os.path.dirname(sys.argv[0]))).absolute(), "config.ini"
)

int_configPath = os.getenv("cb_config", str(defaultConfigPath))

cfgfile = ConfigParser()
cfgfile.read(int_configPath)
