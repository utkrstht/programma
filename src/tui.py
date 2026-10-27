from textual.app import App, ComposeResult
from textual.widgets import Input
from random import choice


# markiplier ref
class Portrugeese(App):
    def compose(self) -> ComposeResult:
        example_queries = ["\"What is the tech stack of this project?\"", "\"Fix broken tests\"", "\"Fix a TODO in the codebase\""]

        yield Input(placeholder=f"Ask anything... {choice(example_queries)}")

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
