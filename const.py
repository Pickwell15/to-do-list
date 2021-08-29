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
	PUBLIC | todo_dir : str
	PUBLIC | menu_item : tuple[str, ...]
	PUBLIC | max_line_length : int
	"""

	# file directories
	todo_dir: str = r"./todo.json"

	# menu
	menu_items: tuple[str, ...] = ("View items", "New item", "Delete item", "Quit")

	# max lengths
	max_line_length: int = 85


# error messages
class Err(Enum):
	"""
	PUBLIC | invalid_menu_number : str
	PUBLIC | invalid_item_number : str
	PUBLIC | no_todo_items_found : str
	PUBLIC | file_not_found : str
	PUBLIC | empty_title : str
	PUBLIC | empty_body : str
	"""

	# invalid
	invalid_menu_number: str = "\nERROR: Invalid number entered. Please try again..."
	invalid_item_number: str = "\nERROR: Invalid item number. Please try again..."

	# not found
	no_todo_items_found: str = "\nERROR: No to-do items found. Try creating one..."
	file_not_found: str = "\nERROR: File {} not found"

	# empty
	empty_title: str = "\nERROR: Invalid input. Title was left empty. Please try again..."
	empty_body: str = "\nERROR: Invalid input. Body was left empty. Please try again..."
