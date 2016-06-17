
__all__ = ["GenGenerator"]

class GenGenerator:
    """
    Dummy class that pretends to be gen generator
    """
    def __init__(self):
        self.generated = 0

    def new(self):
        self.generated += 1
        return []

    def random(self):
        return self.new()
