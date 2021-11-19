class Activity:
    
    def __init__(self, sourceId, posx, posy, posz):
        self.sourceId = sourceId
        self.posx = posx
        self.posy = posy
        self.posz = posz
        
        def __repr__(self):
            return "Activity({},{},{},{})".format(self.sourceId, self.posx, self.posy, self.posz)
        