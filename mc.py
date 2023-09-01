from ursina import *
class Game(Ursina):
    def ___init__(self):
        super().___init__()
        window.color=color.white
        window.title = '1st 3d ursina game'
        window.fullscreen_size=(1366, 768)
        windowed_size = window.fullscreen_size / 1.25 
        Light(type='ambitient', color=(0.5, 0.5, 0.5 ,1))
        Light(type='directional', color=(0.5, 0.5, 0.5 ,1), direction=(1,1,1))
        Sky(color=color.white)
        self.map_size=20
        self.n_game()
    def floor(self, map_size):
        self.ground=Entity(model='quad', scale=map_size , color=color.gray, position=(map_size//2, map_size//2, 0))
        self.grid=Entity(model=Grid(map_size,map_size),  scale=map_size ,position=(map_size//2, map_size//2, 0), color=clor.white, thickness=3)

    def n_game(self):
        self.floor(self.map_size)
        
    def control(self,key):
        super().input(key)

    def update(self):
        pass
    
if __name__ == '__main__':
    game=Game()
    update=game.update
    game.run()
