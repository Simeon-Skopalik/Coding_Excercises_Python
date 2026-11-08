class AuditLog:
    """ Context manager that printes START/END, or FAILED if the block raises"""

    def __init__(self, name) -> None:
        self._name = name

    def __enter__(self) -> "AuditLog":
        print(f"START: {self._name}")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        if exc_type is None:
            print(f"END: {self._name}")
        
        else:
            print(f"FAILED {self._name}: {exc_value}")

        return False
    