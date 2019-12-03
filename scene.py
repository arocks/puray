class Scene:
    """Scene has all the information needed for the ray tracing engine"""

    def __init__(self, camera, objects, width, height):
        self.camera = camera
        self.objects = objects
        self.width = width
        self.height = height
