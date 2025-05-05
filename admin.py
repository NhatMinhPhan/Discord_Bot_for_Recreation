# Admin functions
import discord
import os
from discord import app_commands
from typing import Tuple, Union, Iterable, List

def get_roles(guild: discord.Guild, *args: Union[int, Iterable[int,...]]) -> Tuple[discord.Role, ...]:
    """
    Returns a tuple of Discord roles given a guild and multiple IDs as arguments.
    :param guild: discord.Guild: the Guild used to get roles
    :param args: Multiple IDs for the roles, either ints or Iterable[int]
    :return: A tuple of available Discord Roles for their respective input IDs
    """
    assert isinstance(guild, discord.Guild), 'guild is not a discord.Guild object'
    returned: List[discord.Role] = []
    for arg in args:
        if isinstance(arg, Iterable):
            new_roles = [guild.get_role(role_id) for role_id in arg if isinstance(role_id, int)]
            new_roles = [x for x in new_roles if x is not None]
            returned.extend(new_roles)
        elif isinstance(arg, int):
            returned.append(guild.get_role(arg))
    returned = [x for x in returned if isinstance(x, discord.Role)]
    return tuple(returned)

def get_roles_by_names(guild: discord.Guild, *args: Union[str, Iterable[str, ...]]) -> Tuple[discord.Role, ...]:
    """
    Returns a tuple of Discord Roles by name of the Roles
    :param guild: the guild in which roles are sought
    :param args: names of roles to be returned
    :return: a tuple of Discord Roles
    """
    assert isinstance(guild, discord.Guild), 'guild is not a discord.Guild object'
    roles = guild.roles
    for arg in args:
        if isinstance(arg, list):
            for x in arg:

    return
