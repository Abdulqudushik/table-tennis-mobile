from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, BooleanProperty, StringProperty
from kivy.vector import Vector
from kivy.clock import Clock
import random

class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1  # Speed up slightly on impact
            ball.velocity = vel.x, vel.y + offset

class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    
    # --- NEW: Game State tracking properties ---
    game_active = BooleanProperty(True)
    game_over_message = StringProperty("")
    MAX_SCORE = 11

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def check_game_over(self):
        if self.player1.score >= self.MAX_SCORE:
            self.game_active = False
            self.game_over_message = "YOU WIN!\nTap Screen to Restart"
            self.ball.velocity = (0, 0)
        elif self.player2.score >= self.MAX_SCORE:
            self.game_active = False
            self.game_over_message = "GAME OVER\nTap Screen to Restart"
            self.ball.velocity = (0, 0)

    def update(self, dt):
        # Only process ball movement and AI if the match is active
        if self.game_active:
            self.ball.move()

            # Bounce off paddles
            self.player1.bounce_ball(self.ball)
            self.player2.bounce_ball(self.ball)

            # Bounce off top and bottom table borders
            if (self.ball.y < self.y) or (self.ball.top > self.top):
                self.ball.velocity_y *= -1

            # Simple AI for Player 2 (Right Paddle)
            if self.ball.center_y > self.player2.center_y:
                self.player2.y += 4
            elif self.ball.center_y < self.player2.center_y:
                self.player2.y -= 4

            # Scoring Logic
            if self.ball.x < self.x:
                self.player2.score += 1
                self.check_game_over()
                if self.game_active:
                    self.serve_ball(vel=(4, random.choice([-2, 2])))
                    
            if self.ball.x > self.width:
                self.player1.score += 1
                self.check_game_over()
                if self.game_active:
                    self.serve_ball(vel=(-4, random.choice([-2, 2])))

    # --- TOUCH CONTROLS ---
    def on_touch_down(self, touch):
        # If the game is over, a simple tap anywhere on screen resets the match
        if not self.game_active:
            self.player1.score = 0
            self.player2.score = 0
            self.game_active = True
            self.game_over_message = ""
            self.serve_ball(vel=(4 * random.choice([1, -1]), random.choice([-2, 2])))
            return True
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if self.game_active and touch.x < self.width / 3:
            self.player1.center_y = touch.y

class PongMobileApp(App):
    def build(self):
        game = PongGame()
        
        # --- FIXED: Randomize the very first serve direction ---
        initial_speed_x = 5 * random.choice([1, -1])
        initial_speed_y = random.choice([-2, 2])
        game.serve_ball(vel=(initial_speed_x, initial_speed_y))
        
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == '__main__':
    PongMobileApp().run()