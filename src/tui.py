from textual.app import App, ComposeResult
from textual.widgets import Input, Select, Static
from textual.containers import Vertical
from random import choice

from providers.groq import groq_init, groq_list_models

# markiplier ref
class Portrugeese(App):
    CSS_PATH = "tui.tcss"
    def __init__(self):
        super().__init__()

        # Initialize provider interfaces
        # TODO: handle this based on logged in provider and selected model
        self.client = groq_init()

        # Default selected model
        self.active_model = "openai/gpt-oss-120b"

    def compose(self) -> ComposeResult:
        example_queries = ["\"What is the tech stack of this project?\"", "\"Fix broken tests\"", "\"Fix a TODO in the codebase\""]

        models = groq_list_models(self.client)

        with Vertical(id='main'):
            yield Select.from_values(models, value=self.active_model, allow_blank=False, id='model-menu')

            with Vertical(id='prompt-box'):
                yield Input(placeholder=f"Ask anything... {choice(example_queries)}", id='chat-input')
                yield Static(f"\n{self.active_model}", id='model-label')

    def on_select_changed(self, event: Select.Changed) -> None:
        if event.select.id != "model-menu" or event.value is Select.BLANK:
            return
        self.active_model = str(event.value)
        self.query_one('#model-label', Static).update(f"\n{self.active_model}")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        user_input = event.value
        input_widget = event.input

        # Horrible way of handling this but this is just to get like a basic thing going so it's okay
        if user_input == "/models":
            select_widget = self.query_one('#model-menu', Select)
            select_widget.action_show_overlay()

        if user_input in ["qq", "quit", "exit"]:
            self.exit()

        # Clear input field once submitted
        input_widget.value = ""

