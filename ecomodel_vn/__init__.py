"""EcoModel-VN: lightweight hydrological and terrain-analysis research foundation."""

# version number without 'v' at start
__version__ = "0.1.0.dev0"

# submodules
from . import gis_utils, regions

# public functions
from .core_conversion import d8_to_ldd, ldd_to_d8
from .core_nextxy import read_nextxy
from .dem import fill_depressions, slope
from .flwdir import Flwdir, from_dataframe
from .ecomodel_vn import FlwdirRaster, from_array, from_dem

__all__ = [
    "Flwdir",
    "FlwdirRaster",
    "from_array",
    "from_dataframe",
    "from_dem",
    "read_nextxy",
    "gis_utils",
    "regions",
    "slope",
    "fill_depressions",
    "d8_to_ldd",
    "ldd_to_d8",
]
