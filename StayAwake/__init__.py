import logging
import platform

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


SYSTEM = platform.system().lower()

if SYSTEM == "windows":
    from StayAwake._win import set_keepawake, unset_keepawake
else:
    def set_keepawake(): return None
    def unset_keepawake(): return None
