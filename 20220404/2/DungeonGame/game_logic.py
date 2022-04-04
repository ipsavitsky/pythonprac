"""All functions for game logic."""

from dataclasses import dataclass


@dataclass
class Monster:
    """
    Monster class. Allows to store name and hp of monster.
    """

    name: str
    hp: int

    def __str__(self):
        """
        Stringify a monster
        """
        return f"{self.name} {self.hp} hp"


def print_field(dung_map):
    """print_field.

    :param dung_map: map of the dungeon to print(a list of list of list of monsters)
    :type dung_map: list[list[list[Monster]]]
    """
    for x, row in enumerate(dung_map):
        for y, cell in enumerate(row):
            for monster in cell:
                print(f"{monster.name} at ({x} {y}) hp {monster.hp}")


def move_and_bound_check(arg, dungeon):
    """move_and_bound_check.

    :param arg: direction to move(up, down, left, right)
    :type arg: str
    :param dungeon: dungeon to move in
    :type dung_map: list[list[list[Monster]]]
    """
    move_successful = True
    match arg:
        case "up":
            if dungeon.player_coords[0] + 1 > 9:
                move_successful = False
            else:
                dungeon.player_coords[0] += 1
        case "down":
            if dungeon.player_coords[0] - 1 < 0:
                move_successful = False
            else:
                dungeon.player_coords[0] -= 1
        case "left":
            if dungeon.player_coords[1] - 1 < 0:
                move_successful = False
            else:
                dungeon.player_coords[1] -= 1
        case "right":
            if dungeon.player_coords[1] + 1 > 9:
                move_successful = False
            else:
                dungeon.player_coords[1] += 1
        case _:
            move_successful = False

    if move_successful:
        x, y = dungeon.player_coords
        print(f"player at {x} {y}")
        if dungeon.dungeon[x][y]:
            print(f'ecountered: {", ".join(map(str, dungeon.dungeon[x][y]))}')
        else:
            print("cannot move")


def attack(arg, dungeon):
    """attack.

    :param arg: name of the monster to attack
    :type arg: str
    :param dungeon: dungeon to attack in
    :type dungeon: list[list[list[Monster]]]
    """
    monster_damaged = False
    x, y = dungeon.player_coords
    for monster in dungeon.dungeon[x][y]:
        if monster.name == arg:
            monster_damaged = True
            monster.hp -= 10
            if monster.hp > 0:
                print(f"{monster.name} lost 10 hp, now has {monster.hp} hp")
            else:
                print(f"{monster.name} dies")
                dungeon.dungeon[x][y].remove(monster)
            break
    if not monster_damaged:
        print(f"no {arg} here")
