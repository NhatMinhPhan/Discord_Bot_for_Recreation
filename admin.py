# Admin functions
import discord
from typing import Tuple, List

def get_roles(guild: discord.Guild, *args: int) -> Tuple[discord.Role, ...]:
    """
    Returns a tuple of Discord roles given a guild and multiple IDs as arguments.
    :param guild: discord.Guild: the Guild used to get roles
    :param args: Multiple IDs for the roles (int)
    :return: A tuple of available Discord Roles for their respective input IDs
    """
    assert isinstance(guild, discord.Guild), 'guild is not a discord.Guild object'
    returned: List[discord.Role] = []
    for arg in args:
        assert isinstance(arg, int), 'One of the arguments passed is not an int'
        returned.append(guild.get_role(arg))
    returned = [x for x in returned if isinstance(x, discord.Role)]
    return tuple(returned)

def get_roles_by_names(guild: discord.Guild, *args: str) -> Tuple[discord.Role, ...]:
    """
    Returns a tuple of Discord Roles by name of the Roles
    :param guild: the guild in which roles are sought (discord.Guild)
    :param args: names of roles to be returned (str)
    :return: a tuple of Discord Roles
    """
    assert isinstance(guild, discord.Guild), 'guild is not a discord.Guild object'
    roles = guild.roles
    returned_roles: List[discord.Role] = []
    for arg in args:
        assert isinstance(arg, str), 'One of the arguments passed is not a str'
        for role in roles:
            if role.name == arg:
                returned_roles.append(role)
                break
    return tuple(returned_roles)
