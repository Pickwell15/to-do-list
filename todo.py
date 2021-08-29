"""
OBJECTS
---------------
PUBLIC | ToDo

MODULES
---------------
EXTERNAL | dataclasses -> dataclass
"""

from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class ToDo:
	title: str
	body: str
