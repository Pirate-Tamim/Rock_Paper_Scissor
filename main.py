from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.scrollview import ScrollView
import random

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: "50dp", "50dp", "50dp", "50dp"
    spacing: "10dp"
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1  # White background color
        Rectangle:
            size: self.size
            pos: self.pos

    MDLabel:
        text: "Rock, Paper, Scissors Game! "
        halign: "center"
        theme_text_color: "Secondary"
        font_style: "H4"
        bold: True

    MDLabel:
        id: result_label
        text: "Choose: Rock, Paper, or Scissors"
        halign: "center"
        theme_text_color: "Primary"
        font_style: "H6"

    MDLabel:
        id: score_label
        text: "Score: 0"
        halign: "center"
        theme_text_color: "Primary"
        font_style: "H6"

    ScrollView:
        MDGridLayout:
            cols: 3
            size_hint_y: None
            height: "100dp"
            spacing: "20dp"

            MDRaisedButton:
                text: "Rock"
                on_release: app.play_game("Rock")
                size_hint: None, None
                size: "120dp", "40dp"
                md_bg_color: app.theme_cls.primary_color

            MDRaisedButton:
                text: "Paper"
                on_release: app.play_game("Paper")
                size_hint: None, None
                size: "120dp", "40dp"
                md_bg_color: app.theme_cls.primary_color

            MDRaisedButton:
                text: "Scissors"
                on_release: app.play_game("Scissors")
                size_hint: None, None
                size: "120dp", "40dp"
                md_bg_color: app.theme_cls.primary_color

    MDCard:
        size_hint: None, None
        size: "280dp", "120dp"
        pos_hint: {"center_x": 0.5}
        elevation: 10
        padding: "20dp"

        MDLabel:
            id: final_result
            text: ""
            halign: "center"
            theme_text_color: "Custom"
            text_color: [0, 0, 0, 1]
            font_style: "H6"

    MDLabel:
        text: "Made by GPT And Tamim"
        theme_text_color: "Secondary"
        font_style: "Body1"
        size_hint: None, None
        size: "200dp", "30dp"
        pos_hint: {"center_x": 0.5, "y": 0}  # Positioned it at the bottom middle
        halign: "center"
'''

class RockPaperScissorsApp(MDApp):
    def build(self):
        self.score = 0  # Initialize score
        return Builder.load_string(KV)

    def play_game(self, user_choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        result = self.check_winner(user_choice, computer_choice)

        # Update the result and score
        self.root.ids.result_label.text = f"You: {user_choice}\nComputer: {computer_choice}"
        self.root.ids.final_result.text = result

        # Update the score based on the result
        if result == "You Win!":
            self.score += 1
        elif result == "You Lose!":
            self.score -= 1
        # Update the score label
        self.root.ids.score_label.text = f"Score: {self.score}"

    def check_winner(self, user, computer):
        if user == computer:
            return "It's a Tie!"
        elif (user == "Rock" and computer == "Scissors") or \
             (user == "Scissors" and computer == "Paper") or \
             (user == "Paper" and computer == "Rock"):
            return "You Win!"
        else:
            return "You Lose!"

if __name__ == "__main__":
    RockPaperScissorsApp().run()