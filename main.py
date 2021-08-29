"""
METHODS
---------------
PUBLIC | run -> None

OBJECTS
---------------
PUBLIC | Main

MODULES
---------------
LOCAL | todo -> ToDo
LOCAL | const -> Const, Err
EXTERNAL | typing -> Union
EXTERNAL | sys -> exit
EXTERNAL | time -> sleep
EXTERNAL | json -> loads, dumps
EXTERNAL | pathlib -> Path
EXTERNAL | asyncio -> run
"""

from todo import ToDo
from const import Const, Err

from sys import exit as die
from time import sleep
from json import loads, dumps
from pathlib import Path
from asyncio import run as async_run


class Main:
    """
    METHODS
    ---------------
    PRIVATE | __new__ -> object
    PRIVATE | __init__ -> None
    PRIVATE | __str__ -> str
    PUBLIC | run -> None
    PRIVATE | _menu -> None
    PRIVATE | _display -> None
    PRIVATE | _create -> None
    PRIVATE | _delete -> None
    PRIVATE | _save -> None
    PUBLIC | read_json -> list | dict
    """

    def __new__(cls) -> object:
        """
        Is ran when an instance of the class is created.

        :return: object
        """

        return object.__new__(cls)

    def __init__(self) -> None:
        """
        Is ran when an instance of the class is created.
        Initialises a list of all saved contacts.

        :return: None
        """

        self._todo: list = [eval(item) for item in self.read_json(Const.TODO_DIR.value)]  # initialises local list

    def __str__(self) -> str:
        """
        Returns information about the class.

        :return: str
        """

        return f"Main class. Reading from: '{Const.TODO_DIR.value}'"

    def run(self) -> None:
        """
        Is ran to start program.

        :return: None
        """

        self._menu()

    def _menu(self) -> None:
        """
        Displays a menu for the user to select what they would like to do.

        :return: None
        """

        while 1:
            sleep(0.5)
            print("\nPlease enter the number of the function you would like to execute:")
            for index, item in enumerate(Const.MENU_ITEMS.value):
                print(f"\t[{index+1}] {item}")
            sleep(0.5)

            try:
                match int(input()):
                    case 1:
                        self._display()
                    case 2:
                        self._create()
                    case 3:
                        self._delete()
                    case 4:
                        die()
                    case _:
                        print(Err.INVALID_MENU_NUMBER.value)
            except ValueError:
                print(Err.INVALID_MENU_NUMBER.value)

    def _display(self) -> None:
        """
        Displays a list of saved to-do's.

        :return: None
        """

        if self._todo:
            for index, item in enumerate(self._todo):
                print(f"\t{item.title}")

                '''
                if len(item.body) > self.__MAX_LINE_LENGTH:
                    for i in range(0, len(item.body), self.__MAX_LINE_LENGTH):
                        print(f"\t\t{item.body[i:i+self.__MAX_LINE_LENGTH]}")
                else:
                    print(f"\t\t{item.body}")
                '''
                print('\n'.join([f"\t\t{item.body[i:i+Const.MAX_LINE_LENGTH.value]}" for i in range(0, len(item.body), Const.MAX_LINE_LENGTH.value)])) if len(item.body) > Const.MAX_LINE_LENGTH.value else print(f"\t\t{item.body}")
                print() if index != len(self._todo) else None
        else:
            print(Err.NO_TODO_ITEMS_FOUND.value)

    def _create(self) -> None:
        """
        Displays menu for user to create to-do.

        :return: None
        """

        print("\nNEW TO-DO ITEM:")

        while 1:
            title: str = input("\n\tEnter the title of the to-do: ").title()
            if title:
                break
            else:
                print(Err.EMPTY_TITLE.value)

        while 1:
            body: str = input("\tEnter the body of the to-do: ").capitalize()
            if body:
                break
            else:
                print(Err.EMPTY_BODY.value)

        self._todo.append(ToDo(title, body))  # add to local list
        async_run(self._save())  # save to file

    def _delete(self) -> None:
        """
        Displays menu for user to choose which contact to delete.

        :return: None
        """

        for index, item in enumerate(self._todo):
            print(f"\t[{index+1}] {item.title}")

        try:
            index = int(input()) - 1
            if index <= len(self._todo):
                self._todo.pop(index)  # remove contact from list
                async_run(self._save())  # save to file
            else:
                print(Err.INVALID_ITEM_NUMBER.value)
        except ValueError:
            print(Err.INVALID_ITEM_NUMBER.value)

    async def _save(self) -> None:
        """
        Saves to-do's to savefile.
        Asynchronous.

        :return: None
        """

        open(Const.TODO_DIR.value, "w").write(dumps([repr(item) for item in self._todo], sort_keys=True, indent=4))

    @classmethod
    def read_json(cls, path: str) -> list | dict:
        """
        Returns JSON data from a specified file if the file exists.
        Else exits program and displays error.

        :param str path: The directory to read the JSON data from

        :return: Union[list, dict]
        """
        return loads(open(path, "r").read()) if Path(path).is_file() else die(Err.FILE_NOT_FOUND.value.format(path))


def run() -> None:
    """
    Create instance of 'Main' class.
    Run 'Main' class.

    :return: None
    """

    main: Main = Main()
    main.run()


if __name__ == "__main__":
    run()
