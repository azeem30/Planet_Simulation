import pygame
import math
import calendargui
import planet_details
from PyQt5 import QtCore, QtGui, QtWidgets

pygame.init()
run = True
WIDTH, HEIGHT = 800, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")
__total_days__ = calendargui.total_days
mouse_pos = ()
# COLORS(R,G,B)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
WHITE = (255, 255, 255)
AMBER = (255, 190, 0)
DARK_GREY = (80, 78, 81)

with open("details.txt", "r") as details:
    data = details.read()[:]
    lines_of_data = data.split("\n")
    planet_names = lines_of_data[0].split(",")
    planet_masses = lines_of_data[1].split(",")
    planet_radii = lines_of_data[2].split(",")
    planet_descs = lines_of_data[3].split(",")

class Planet:

    AU = 149.6e6*1000
    G = 6.67428e-11
    SCALE = 200 / AU  # 1 AU = 100pixels
    TIMESTEP = 3600*24  # 1 Day

    def __init__(self, x, y, radius, color, mass, name):
        self.details_window = None
        self.circle = None
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.name = name
        self.orbits = None
        self.orbit = []
        self.sun = False
        self.mercury = False
        self.venus = False
        self.earth = False
        self.mars = False
        self.distance_to_sun = 0
        self.labels_desc_font = pygame.font.SysFont('Arial', 18)
        self.mercury_label = self.labels_desc_font.render("Mercury", True, DARK_GREY)
        self.venus_label = self.labels_desc_font.render("Venus", True, AMBER)
        self.earth_label = self.labels_desc_font.render("Earth", True, BLUE)
        self.mars_label = self.labels_desc_font.render("Mars", True, RED)

# Adding Velocity
        self.x_val = 0
        self.y_val = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + WIDTH / 2
                updated_points.append((x, y))
            self.orbits = pygame.draw.lines(win, self.color, False, updated_points, 2)
        self.circle = pygame.draw.circle(win, self.color, (x, y), self.radius)

        # To display the distance between each Planet and the Sun
        if not self.sun:
            font = pygame.font.SysFont('Arial', 16)
            text_distance_from_sun = font.render(f'{self.distance_to_sun / Planet.AU:.4f} AU', True, YELLOW)
            win.blit(text_distance_from_sun, (x + self.radius + 5, y - 10))

        # To display the distance between Each Planet and the Earth
        if not self.sun:
            distance_to_earth = int(abs(self.distance_to_sun - (1 * Planet.AU)) / 1000)
            font = pygame.font.SysFont('Serif', 16)
            text_distance_from_earth = font.render(f'{distance_to_earth / Planet.AU:.4f} AU', True, BLUE)
            win.blit(text_distance_from_earth, (x, y+20))

        labels_desc_sun = self.labels_desc_font.render('YELLOW: DISTANCE FROM THE SUN', True, YELLOW)
        win.blit(labels_desc_sun, (530, 10))

        labels_desc_earth = self.labels_desc_font.render('BLUE: DISTANCE FROM THE EARTH', True, BLUE)
        win.blit(labels_desc_earth, (530, 30))

        if self.mercury:
            win.blit(self.mercury_label, (x, y-30))
            pygame.draw.rect(win, DARK_GREY, self.mercury_label.get_rect(), 2)

        if self.venus:
            win.blit(self.venus_label, (x, y-35))

        if self.earth:
            win.blit(self.earth_label, (x, y-40))

        if self.mars:
            win.blit(self.mars_label, (x, y-35))

# Distance between two objects
    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x**2 + distance_y**2)

        if other.sun:
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass / distance**2
        #atan2 special library in math which will calculate y over x and give the angle
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

# Force from different planets
    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy
        # a = f/m

        self.x_val += total_fx / self.mass * self.TIMESTEP
        self.y_val += total_fy / self.mass * self.TIMESTEP
        self.x += self.x_val * self.TIMESTEP
        self.y += self.y_val * self.TIMESTEP
        self.orbit.append((self.x, self.y))

        # F = m * a

    def clicked_planet(self, click_point):
        if self.mercury:
            circle_pos = self.circle.center
            distance = ((click_point[0] - circle_pos[0]) ** 2 + (click_point[1] - circle_pos[1]) ** 2) ** 0.5
            if distance <= self.radius:
                self.display_details(self.name)
        elif self.venus:
            circle_pos = self.circle.center
            distance = ((click_point[0] - circle_pos[0]) ** 2 + (click_point[1] - circle_pos[1]) ** 2) ** 0.5
            if distance <= self.radius:
                self.display_details(self.name)
        elif self.earth:
            circle_pos = self.circle.center
            distance = ((click_point[0] - circle_pos[0]) ** 2 + (click_point[1] - circle_pos[1]) ** 2) ** 0.5
            if distance <= self.radius:
                self.display_details(self.name)
        elif self.mars:
            circle_pos = self.circle.center
            distance = ((click_point[0] - circle_pos[0]) ** 2 + (click_point[1] - circle_pos[1]) ** 2) ** 0.5
            if distance <= self.radius:
                self.display_details(self.name)
        elif self.sun:
            circle_pos = self.circle.center
            distance = ((click_point[0] - circle_pos[0]) ** 2 + (click_point[1] - circle_pos[1]) ** 2) ** 0.5
            if distance <= self.radius:
                self.display_details(self.name)

    def display_details(self, planet_name):
        global planet_names, planet_masses, planet_radii, planet_descs
        self.details_window = QtWidgets.QWidget()
        self.details_ui = planet_details.Ui_Form()
        self.details_ui.setupUi(self.details_window)
        self.details_window.show()
        try:
            if planet_name == "mercury":
                self.details_ui.planet_image.setPixmap(QtGui.QPixmap("mercury_image.jpg"))
                self.details_ui.planet_image.setScaledContents(True)
                self.details_ui.edit_name.setText(planet_names[0])
                self.details_ui.edit_mass.setText(planet_masses[0])
                self.details_ui.edit_radius.setText(planet_radii[0])
                self.details_ui.edit_desc.setText(planet_descs[0])
            elif planet_name == "venus":
                self.details_ui.planet_image.setPixmap(QtGui.QPixmap("venus_image.jpg"))
                self.details_ui.planet_image.setScaledContents(True)
                self.details_ui.edit_name.setText(planet_names[1])
                self.details_ui.edit_mass.setText(planet_masses[1])
                self.details_ui.edit_radius.setText(planet_radii[1])
                self.details_ui.edit_desc.setText(planet_descs[1])
            elif planet_name == "earth":
                self.details_ui.planet_image.setPixmap(QtGui.QPixmap("earth_image.jpg"))
                self.details_ui.planet_image.setScaledContents(True)
                self.details_ui.edit_name.setText(planet_names[2])
                self.details_ui.edit_mass.setText(planet_masses[2])
                self.details_ui.edit_radius.setText(planet_radii[2])
                self.details_ui.edit_desc.setText(planet_descs[2])
            elif planet_name == "mars":
                self.details_ui.planet_image.setPixmap(QtGui.QPixmap("mars_image.jpg"))
                self.details_ui.planet_image.setScaledContents(True)
                self.details_ui.edit_name.setText(planet_names[3])
                self.details_ui.edit_mass.setText(planet_masses[3])
                self.details_ui.edit_radius.setText(planet_radii[3])
                self.details_ui.edit_desc.setText(planet_descs[3])
            elif planet_name == "sun":
                self.details_ui.planet_image.setPixmap(QtGui.QPixmap("sun_image.jpg"))
                self.details_ui.planet_image.setScaledContents(True)
                self.details_ui.planet_name.setText("Star")
                self.details_ui.edit_name.setText(planet_names[4])
                self.details_ui.edit_mass.setText(planet_masses[4])
                self.details_ui.edit_radius.setText(planet_radii[4])
                self.details_ui.edit_desc.setText(planet_descs[4])
        except Exception as exception:
            print(str(exception))
def main():
    global run, mouse_pos
    run = True
    clock = pygame.time.Clock()
    elapsed_days = 0

    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10 ** 30, "sun")
    sun.sun = True

    mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GREY, 0.330 * 10 ** 24, "mercury")
    mercury.y_val = -47.4 * 1000
    mercury.mercury = True

    venus = Planet(0.723 * Planet.AU, 0, 14, AMBER, 4.8685 * 10 ** 24, "venus")
    venus.y_val = -35.02 * 1000
    venus.venus = True

    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10 ** 24, "earth")
    earth.y_val = 29.783 * 1000
    earth.earth = True

    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10 ** 23, "mars")
    mars.y_val = 24.077 * 1000
    mars.mars = True

    planets = [sun, mercury, venus, earth, mars]
    while run:
        clock.tick(120)  # Run this event 120frames per second
        win.fill((0, 0, 0))
        # pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for planet in planets:
                    planet.clicked_planet(mouse_pos)

        elapsed_days += 1
        for planet in planets:
            if elapsed_days < __total_days__:
                planet.update_position(planets)
                planet.draw(win)
            else:
                planet.draw(win)

        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
    del __total_days__



