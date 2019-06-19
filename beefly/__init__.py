from tensorview.train import PlotMetrics
from tensorview.train import PlotMetricsOnBatch
from tensorview.train import PlotMetricsOnEpoch
from tensorview.train import __beefly_version__
import warnings
warnings.warn("""
Beely will no longer add new features in the future, 
but will continue to maintain bug fixes for existing versions. 
Now that we have replaced it with a new library, 
use the command `pip install tensorview` to install the new toolkit to use.
For more information, please visit `https://github.com/Hourout/tensorview`.
""")

__version__ = __beefly_version__
__author__ = 'JinQing Lee'
