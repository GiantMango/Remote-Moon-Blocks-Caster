import pygame
import os
import random
import re


"""
====================== Global Variables ======================
"""
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
FRAME = 2
SCREEN = None
SCALE_FACTOR = 2
TEXT_COLOR = (10, 10, 10)


"""
====================== Class definition ======================
"""


class PgObject:
    def __init__(self, pgObject, x=0, y=0, centerx=False):
        self.pgObject = pgObject
        self.x = x
        self.y = y
        self.index = 0
        self.isList = isinstance(self.pgObject, list)

        if self.isList:
            (self.width, self.height) = self.pgObject[self.index].get_size()
        else:
            (self.width, self.height) = self.pgObject.get_size()

        ## Dynamic position
        if centerx:
            self.x = (WINDOW_WIDTH - self.width) / 2

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface):
        if self.isList:
            length = len(self.pgObject)
            surface.blit(self.pgObject[self.index % length], (self.x, self.y))
        else:
            surface.blit(self.pgObject, (self.x, self.y))

    def __str__(self):
        return f"This is a {self.pgObject}"


class Image(PgObject):
    def __init__(self, image, x=0, y=0, centerx=False):
        super().__init__(image, x, y, centerx=centerx)
        self.rotateCount = 0

    def __str__(self):
        return "\n".join([f"This is {i}" for i in self.pgObject])


class Text(PgObject):
    def __init__(self, text, x=0, y=0, centerx=False):
        super().__init__(text, x, y, centerx=centerx)

    def __str__(self):
        return f"This is a text image: '{self.pgObject}'"


class Button(PgObject):
    def __init__(self, image, x=0, y=0, centerx=False):
        super().__init__(image, x, y, centerx=centerx)

        self.index = 0
        self.start = False

        self.rect = self.pgObject[self.index].get_rect(topleft=(self.x, self.y))

    def draw(self, surface):
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.start:
                self.start = True
                self.index = 1

        if self.start == False:
            self.index = 0

        surface.blit(self.pgObject[self.index], (self.rect.x, self.rect.y))


"""
====================== main function ======================
"""


def main():
    global FRAME, WINDOW_WIDTH, WINDOW_HEIGHT, SCREEN

    pygame.init()

    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Remote God")
    font = pygame.font.SysFont(None, 30)

    ## get image paths
    gods_path = getPaths("assets/gods")
    cups_path = getPaths("assets/cup")
    btns_path = getPaths("assets/buttons")

    gods_names = [re.match(r"^.*/(.*)\.png$", p).groups()[0] for p in gods_path]

    ## load as pygame image elements
    gods = loadImgObject(gods_path)
    gods_gray = loadImgObject(gods_path, isGray=True, scale_factor=1.5)
    cupRight = loadImgObject(cups_path, isFlip=True)
    cupLeft = loadImgObject(cups_path)
    btns = loadImgObject(btns_path)
    arrowRight = loadImgObject(["assets/arrow.png"], scale_factor=1)
    arrowLeft = loadImgObject(["assets/arrow.png"], isFlip=True, scale_factor=1)

    ## turn into pygame objects
    gods = Image(gods, y=70, centerx=True)
    godLeft = Image(gods_gray)
    godLeft.set_position(x=(WINDOW_WIDTH - godLeft.width) / 2 + 120, y=70)
    godRight = Image(gods_gray)
    godRight.set_position(x=(WINDOW_WIDTH - godRight.width) / 2 - 120, y=70)

    cupRight = Image(cupRight)
    cupRight.set_position(x=(WINDOW_WIDTH - cupRight.width) / 2 + 80, y=270)
    cupLeft = Image(cupLeft)
    cupLeft.set_position(x=(WINDOW_WIDTH - cupRight.width) / 2 - 80, y=270)

    arrowRight = Image(arrowRight)
    arrowRight.set_position(x=(WINDOW_WIDTH - arrowRight.width) / 2 + 100, y=180)
    arrowLeft = Image(arrowLeft)
    arrowLeft.set_position(x=(WINDOW_WIDTH - arrowLeft.width) / 2 - 100, y=180)

    buttons = Button(btns, y=420, centerx=True)

    ## Text elements
    description = Text(
        font.render("Click THROW to get answer.", True, TEXT_COLOR), y=230, centerx=True
    )

    god_name = Text(
        font.render(gods_names[gods.index], True, TEXT_COLOR), y=30, centerx=True
    )

    clock = pygame.time.Clock()
    rotate_count = 0
    key_pressed = False
    running = True

    """
    ====================== pygame main loop ======================
    """
    while running:
        clock.tick(24)  # fps

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                key_pressed = True

        ## start animation
        if buttons.start:
            if rotate_count < 24:
                cupLeft.index = rotate_count % 4
                cupRight.index = rotate_count % 4
                rotate_count += 1
            else:
                buttons.start = False
                rotate_count = 0
                cupLeft.index = random.choice([0, 2])
                cupRight.index = random.choice([0, 2])

                if cupLeft.index != cupRight.index:
                    description = Text(
                        font.render("God says yes!", True, TEXT_COLOR),
                        y=230,
                        centerx=True,
                    )
                else:
                    description = Text(
                        font.render("God says no :(", True, TEXT_COLOR),
                        y=230,
                        centerx=True,
                    )

        ## check key press
        keys = pygame.key.get_pressed()
        if key_pressed:
            if keys[pygame.K_LEFT]:
                gods.index -= 1

            elif keys[pygame.K_RIGHT]:
                gods.index += 1

            key_pressed = False

            god_name = Text(
                font.render(gods_names[gods.index % len(gods_names)], True, TEXT_COLOR),
                y=30,
                centerx=True,
            )

        godLeft.index = gods.index - 1
        godRight.index = gods.index + 1

        redrawWindow(
            gods,
            cupLeft,
            cupRight,
            buttons,
            god_name,
            description,
            godLeft,
            godRight,
            arrowLeft,
            arrowRight,
        )

    pygame.quit()


"""
====================== Helper Functions ======================
"""


def getPaths(folder_path):
    path_list = [f"{folder_path}/{f}" for f in os.listdir(folder_path + "/")]
    return sorted(path_list)


def loadImgObject(path_list, isFlip=False, isGray=False, scale_factor=SCALE_FACTOR):

    images_list = [
        pygame.transform.scale_by(pygame.image.load(f).convert_alpha(), scale_factor)
        for f in sorted(path_list)
    ]

    if isFlip:
        images_list = [
            pygame.transform.flip(i, flip_y=False, flip_x=True) for i in images_list
        ]

    if isGray:
        images_list = [pygame.transform.grayscale(i) for i in images_list]

    return images_list


def redrawWindow(*image):
    SCREEN.fill((235, 228, 228))

    for img in image:
        img.draw(SCREEN)

    pygame.display.update()


if __name__ == "__main__":
    main()
