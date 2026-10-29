from commands.registry import command, registry

from tui import Portrugeese

@command("help", help="Show available commands", aliases=("h"))
def help(app: Portrugeese, args: list[str]) -> None:
    lines = [f"{cmd.invocation} {cmd.help}" for cmd in registry.all()]
    app.notify("\n".join(lines), title="Commands")

