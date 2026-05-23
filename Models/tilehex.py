class TileHex:
  def __init__(self, type: tuple[int, int], 
                     hexes: tuple[TileHex, TileHex],
                     level: int = 1): 
    self.type = type       
    self.hexes = hexes    
    self.level = level     
    pass