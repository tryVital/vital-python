try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata  # type: ignore

try:
    __version__ = importlib_metadata.version("vital")
except Exception:
    __version__ = "Undefined"
