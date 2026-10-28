from textual.app import App, ComposeResult
from textual.widgets import Input, Select
from textual.containers import Vertical
from random import choice

from llm import groq_init, groq_list_models

# markiplier ref
class Portrugeese(App):
    def __init__(self):
        super().__init__()

        # Initialize provider interfaces
        self.client = groq_init()

        # Default selected model
        self.active_model = "openai/gpt-oss-120b"

    def compose(self) -> ComposeResult:
        example_queries = ["\"What is the tech stack of this project?\"", "\"Fix broken tests\"", "\"Fix a TODO in the codebase\""]

        models = groq_list_models(self.client)

        with Vertical():
            yield Select.from_values(models, value=self.active_model, allow_blank=False)
            yield Input(placeholder=f"Ask anything... {choice(example_queries)}")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        user_input = event.value
        input_widget = event.input

        # Horrible way of handling this but this is just to get like a basic thing going so it's okay
        if user_input == "/models":
            pass

        if user_input in ["qq", "quit", "exit"]:
            self.exit()

        # Clear input field once submitted
        input_widget.value = ""

if __name__ == "__main__":
    app = Portrugeese()
    app.run()
