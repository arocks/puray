#!/usr/bin/env python
"""Puray - a Pure Python Raytracer by Arun Ravindran, 2019"""
import argparse
import math
from random import randint

from color import Color
from engine import RenderEngine
from light import Light
from material import Material
from point import Point
from scene import Scene
from sphere import Sphere
from vector import Vector


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("imageout", help="Path to rendered image")
    args = parser.parse_args()
    WIDTH = 1920
    HEIGHT = 1080
    camera = Vector(0, 0, -1)
    lights = [Light(Point(1.5, -0.5, -10.0), Color.from_hex("#FF4900"))]
    # Model of the Corona Virus (relative measurements from Inkscape mockup)
    radius = 0.2
    spikes = 32
    stem_length = 3
    stem_radius = 0.008
    blob_radius = 0.01
    # Add core
    objects = [Sphere(Point(0, 0, 0), radius, Material(Color.from_hex("#FF7701")))]
    # Add spiky blob filaments
    for i in range(spikes):
        angle = math.radians(360.0 / spikes * i + randint(-2, 2))
        for j in range(stem_length):
            # convert polar coordinates into Cartesian coordinates
            x = (radius + stem_radius * j) * math.sin(angle)
            y = (radius + stem_radius * j) * math.cos(angle)
            objects.append(
                Sphere(Point(x, y, 0), stem_radius, Material(Color.from_hex("#d47721")))
            )
        # ending blob
        x = (radius + stem_radius * j + blob_radius) * math.sin(angle)
        y = (radius + stem_radius * j + blob_radius) * math.cos(angle)
        objects.append(
            Sphere(Point(x, y, 0), blob_radius, Material(Color.from_hex("#febd14")))
        )

    scene = Scene(camera, objects, lights, WIDTH, HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)

    with open(args.imageout, "w") as img_file:
        image.write_ppm(img_file)


if __name__ == "__main__":
    main()
