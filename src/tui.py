from textual.app import App, ComposeResult
from textual.widgets import Input

# markiplier ref
class Portrugeese(App):
    def compose(self) -> ComposeResult:
        # TODO: random example questions in placeholder (e.g "What is the tech stack of this project?")
        yield Input(placeholder="Ask anything...")

if __name__ == "__main__":
    app = Portrugeese()
    app.run()
