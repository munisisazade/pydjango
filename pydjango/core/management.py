import os
import sys
from pydjango.core.command import CommandParser
from pydjango.core.utils.color import color_style


class ManagementUtility(object):
    """
    Encapsulate the logic of the CLI utilities.
    """

    def __init__(self, argv=None):
        self.argv = argv or sys.argv[:]
        self.prog_name = os.path.basename(self.argv[0])
        self.style = color_style()
        self.filename = None
        if self.prog_name == '__main__.py':
            self.prog_name = 'python -m pydjango'
        self.settings_exception = None

    def main_help_text(self, commands_only=False):
        """Return the script's main help text, as a string."""
        usage = [
            "",
            "😄 %s is a CLI tool that provisions and manages django application optimized for development workflows." % self.prog_name,
            "",
            "💡💡💡💡💡💡💡Usage:💡",
            "   %s [folder_name]" % self.prog_name,
            "",
            "Available Commands:",
            *self.get_commands(),
            "🚜",
            "Flags:",
            *self.get_flags(),
            ""
        ]

        return '\n'.join(usage)

    def unknown_command(self):
        """Return the script's when command unknown"""
        usage = [
            "",
            "😿 Error: cannot accept `%s` for `%s`" % (self.filename, self.prog_name),
            "",
            "👉👉👉👉👉👉Run '%s --help' for usage." % self.prog_name,
            ""
        ]
        return '\n'.join(usage)

    def file_exist(self):
        """Return the script's when command unknown"""
        usage = [
            "",
            "😿 Error:  `%s` %s already exist " % (self.filename, "folder" if self.dir else "file"),
            "",
            "Run '%s --help' for usage." % self.prog_name,
            ""
        ]
        return '\n'.join(usage)

    def check_file_exist(self):
        self.dir = True if os.path.isdir(self.filename) else False
        if os.path.isdir(self.filename) or os.path.isfile(self.filename):
            sys.stdout.write(self.file_exist())
            sys.exit(1)
        else:
            pass

    def execute(self):
        """
        Given the command-line arguments, figure out which subcommand is being
        run, create a parser appropriate to that command, and run it.
        """
        parser = CommandParser(None, usage="%(prog)s subcommand [options] [args]", add_help=False)
        parser.add_argument('--settings')
        parser.add_argument('--pythonpath')
        parser.add_argument('args', nargs='*')  # catch-all
        options, args = parser.parse_known_args(self.argv[1:])
        #
        # if args:
        #     self.run_args(args)

        if len(options.args) == 1:
            self.filename = options.args[0]
            if self.filename.isalnum():
                self.check_file_exist()

            else:
                sys.stdout.write(self.unknown_command())
                sys.exit(1)
        else:
            sys.stdout.write(self.main_help_text())
            sys.exit(1)

    def get_commands(self):
        return [
            "   folder_name         Application name and base project directory space not allow"
        ]

    def get_flags(self):
        return [
            "   -V, --version       Get %s CLI version" % self.prog_name,
            "   -l, --log           Print aditional logs",
            "   -a, --author        Print author's info",
            "   -g, --git           Application integrate git"
        ]


def execute_from_command_line(argv=None):
    """Run a ManagementUtility."""
    utility = ManagementUtility(argv)
    utility.execute()
