from OpenGL.GL import *


def draw_vector(x, y, z):
    """Рисует вектор от начала координат до заданной точки."""
    glColor3f(1.0, 1.0, 1.0)  # Белый цвет
    glBegin(GL_LINES)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(x, y, z)
    glEnd()


def draw_line(data1, data2):
  """Рисует линию от (x1, y1, z1) до (x2, y2, z2)."""
  x1, y1, z1, = data1
  x2, y2, z2 = data2
  glBegin(GL_LINES)
  glVertex3f(x1, y1, z1)  # Начальная точка
  glVertex3f(x2, y2, z2)  # Конечная точка
  glEnd()