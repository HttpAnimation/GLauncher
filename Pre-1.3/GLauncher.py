import pygame
import tkinter as tk
from tkinter import ttk
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

cube_vertices = [
    (-1, -1, -1),
    (-1, 1, -1),
    (1, 1, -1),
    (1, -1, -1),
    (-1, -1, 1),
    (-1, 1, 1),
    (1, 1, 1),
    (1, -1, 1)
]

cube_edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

pygame.init()

angle_x = 0
angle_y = 0

def rotate_cube():
    global angle_x, angle_y

    angle_x += 1
    angle_y += 1

    rotated_vertices = []
    for vertex in cube_vertices:
        x, y, z = vertex

        y = y * pygame.math.Vector2(1, 0).rotate(angle_x).y - z * pygame.math.Vector2(1, 0).rotate(angle_x).x
        z = y * pygame.math.Vector2(1, 0).rotate(angle_x).x + z * pygame.math.Vector2(1, 0).rotate(angle_x).y

        x = x * pygame.math.Vector2(0, 1).rotate(angle_y).y - z * pygame.math.Vector2(0, 1).rotate(angle_y).x
        z = x * pygame.math.Vector2(0, 1).rotate(angle_y).x + z * pygame.math.Vector2(0, 1).rotate(angle_y).y

        rotated_vertices.append((x, y, z))

    return rotated_vertices

root = tk.Tk()
root.title("Spinning 3D Cube")

pygame_screen = pygame.display.set_mode((400, 400), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Spinning 3D Cube")

gluPerspective = pygame.math.Vector3(0, 0, -5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glBegin(GL_LINES)
    for edge in cube_edges:
        for vertex in edge:
            glVertex3fv(rotate_cube()[vertex])
    glEnd()

    pygame.display.flip()
    pygame.time.wait(10)

    root.update()

pygame.quit()
