import logging
logger = logging.getLogger(__name__)

class AuditLog:
    """ Context manager that logs START/END, or FAILED if the block raises"""

    def __init__(self, name) -> None:
        self._name = name

    def __enter__(self) -> "AuditLog":
        logger.info("START %s", self._name)
        return self
    
    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        if exc_type is None:
            logger.info("END %s", self._name)
        
        else:
            logger.error("FAILED %s: %s", self._name, exc_value)

        return False
    