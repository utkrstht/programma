from dataclasses import dataclass
from typing import Awaitable, Callable, Iterable

from tui import Portrugeese

CommandHandler = Callable[["Portrugeese", list[str]], Awaitable[None] | None]

@dataclass(frozen=True)
class Command:
    name: str
    handler: CommandHandler
    help: str
    usage: str = ""
    aliases: tuple[str, ...] = ()
    hidden: bool = False

    @property
    def invocation(self) -> str:
        return f"/{self.name}" + (f" {self.usage}" if self.usage else "")

class CommandRegistry:
    def __init__(self) -> None:
        self._commands: dict[str, Command] = {}

    def register(self, command: Command) -> Command:
        for key in (command.name, *command.aliases):
            if key in self._commands:
                raise ValueError(f"Command {key} is already registered")

        for key in (command.name, *command.aliases):
            self._commands[key] = command

        return command

    def get(self, name: str) -> Command | None:
        return self._commands.get(name.lstrip("/"))

    def all(self) -> list[Command]:
        unique: dict[str, Command] = {}

        for command in self._commands.values():
            unique.setdefault(command.name, command)

        return [command for command in unique.values() if not command.hidden]

    def names(self) -> list[str]:
        return [command.name for command in self.all()]


registry = CommandRegistry()

def command(name: str, 
            *, 
            help: str, 
            usage: str = "", 
            aliases: Iterable[str] = (), 
            hidden: bool = False
        ) -> Callable[[CommandHandler], CommandHandler]:
    
    def decorator(handler: CommandHandler) -> CommandHandler:
        registry.register(Command(
            name=name,
            handler=handler,
            help=help,
            usage=usage,
            aliases=tuple(aliases),
            hidden=hidden
        ))

        return handler

    return decorator