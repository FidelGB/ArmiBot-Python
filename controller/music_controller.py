"""Music controller
"""
import os
import discord

class MusicController():
    """Music Controller
    """

    def __init__(self, client, message):
        """Constructor

        Args:
            client (Client): Discord client
            message 
        """
        self.message = message

    def load(self, params):
        """Load function

        Args:
            params (list): params list
        """
        command = params[0]
        del params[0]

    def __join(self):
        print("Hello")

    def __get_function_params(self, command):
        commands = {
            "join": self.__join
        }

        return commands.get(command, lambda: None)
