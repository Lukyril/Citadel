from Models.tilehex import TileHex


class Tile:
  def __init__(self, hexes: tuple[TileHex, TileHex, TileHex]):
    self.hexes = hexes
    pass