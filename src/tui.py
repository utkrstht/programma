from textual.app import App, ComposeResult
from textual.widgets import Input

# markiplier ref
class Portrugeese(App):
    def compose(self) -> ComposeResult:
        # TODO: random example questions in placeholder (e.g "What is the tech stack of this project?")
        yield Input(placeholder="Ask anything...")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        user_input = event.value
        input_widget = event.input

        if user_input in ["qq", "quit", "exit"]:
            self.exit()

        # clear input field once submitted
        input_widget.value = ""

if __name__ == "__main__":
    app = Portrugeese()
    app.run()
