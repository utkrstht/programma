from textual.app import App
from textual.widgets import Welcome

# markiplier ref
class Portrugeese(App):
    def compose(self):
        yield Welcome()

    def on_button_pressed(self):
        self.exit()

if __name__ == "__main__":
    app = Portrugeese()
    app.run()
