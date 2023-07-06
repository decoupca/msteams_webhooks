"""Base classes from which other classes inherit."""
from typing import Any


class Entity:
    """Base class for all other entities."""

    def dump(self) -> dict[str, Any]:
        """Convenience alias."""
        return self.serialize()

    def serialize(self) -> dict[str, Any]:
        """Serialize object into data structure."""
        return {}
