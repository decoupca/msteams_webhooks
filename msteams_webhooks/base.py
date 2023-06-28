"""Base classes from which other classes inherit."""
from typing import Any


class Entity:
    """Base class for all other entities."""

    def serialize(self) -> dict[str, Any]:
        """Serialize object into data structure."""
        return {}
