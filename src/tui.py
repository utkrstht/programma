from textual.app import App
from textual.widgets import Input

# markiplier ref
class Portrugeese(App):
    def compose(self):
        # TODO: random example questions in placeholder (e.g "What is the tech stack of this project?")
        yield Input(placeholder="Ask anything...")

    def on_button_pressed(self):
        self.exit()

if __name__ == "__main__":
    app = Portrugeese()
    app.run()
