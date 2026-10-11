from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("etude-engine")
except PackageNotFoundError:
    __version__ = "0+local"
