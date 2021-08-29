"""
OBJECTS
---------------
PUBLIC | Const -> Enum
PUBLIC | Err -> Enum

MODULES
---------------
EXTERNAL | enum -> Enum
"""


from enum import Enum


class Const(Enum):
	"""
	ATTRIBUTES
	----------------
	PUBLIC | TODO_DIR : str
	PUBLIC | MENU_ITEMS : tuple[str, ...]
	PUBLIC | MAX_LINE_LENGTH : int
	"""

	# file directories
	TODO_DIR = r"./todo.json"

	# menu
	MENU_ITEMS = ("View items", "New item", "Delete item", "Quit")

	# max lengths
	MAX_LINE_LENGTH = 85


# error messages
class Err(Enum):
	"""
	ATTRIBUTES
	--------------
	PUBLIC | INVALID_MENU_NUMBER : str
	PUBLIC | INVALID_ITEM_NUMBER : str
	PUBLIC | NO_TODO_ITEMS_FOUNDS : str
	PUBLIC | FILE_NOT_FOUND : str
	PUBLIC | EMPTY_TITLE : str
	PUBLIC | EMPTY_BODY : str
	"""

	# invalid
	INVALID_MENU_NUMBER = "\nERROR: Invalid number entered. Please try again..."
	INVALID_ITEM_NUMBER = "\nERROR: Invalid item number. Please try again..."

	# not found
	NO_TODO_ITEMS_FOUND = "\nERROR: No to-do items found. Try creating one..."
	FILE_NOT_FOUND = "\nERROR: File {} not found"

	# empty
	EMPTY_TITLE = "\nERROR: Invalid input. Title was left empty. Please try again..."
	EMPTY_ROOM = "\nERROR: Invalid input. Body was left empty. Please try again..."
