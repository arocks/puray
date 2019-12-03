class Ray:
    """Ray is a half-line with an origin and a normalized direction"""

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalize()
