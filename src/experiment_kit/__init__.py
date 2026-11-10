"""Portable experiment validation without execution dependencies."""
from .records import validate_record
from .validation import validate_spec

__all__ = ["validate_record", "validate_spec"]
