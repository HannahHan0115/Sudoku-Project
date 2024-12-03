import pygame,sys
class Cell:
    def __init__(self,value,row,col,screen):
        self.value=value
        self.row=row
        self.col=col
        self.screen=screen
        self.sketch_value=0
        self.selected=False
        self.font=pygame.font.SysFont('comicsans',40)
        self.width=50
        self.height=50

    def set_cell_value(self,value):
        self.value=value

    def set_sketched_value(self,value):
        self.sketch_value=value

    def draw(self):
        x=self.col*self.width
        y=self.row*self.height

        if self.selected:
            pygame.draw.rect(self.screen,(255,0,0),(x,y,self.width,self.height),3)

        if self.value!=0:
            cell_content=self.font.render(str(self.value),1,(0,0,0))
            self.screen.blit(cell_content,(x+(self.width//2-cell_content.get_width()//2),y+(self.height // 2 - cell_content.get_height() // 2)))
        if self.sketch_value!=0:
            cell_content=self.font.render(str(self.sketch_value),1,(128,128,128))
            self.screen.blit(cell_content,(x+5,y+5))




