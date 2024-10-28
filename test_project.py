import pygame
from project import getPaths, loadImgObject, redrawWindow


pygame.init()
SCREEN = pygame.display.set_mode((500, 500))


def test_getPaths():
    assert getPaths("assets") == sorted(
        ["assets/arrow.png", "assets/buttons", "assets/cup", "assets/gods"]
    )


def test_loadImgObject(monkeypatch):
    def mock_load(filename):
        return pygame.Surface((50, 50))

    monkeypatch.setattr(pygame.image, "load", mock_load)
    images = loadImgObject(["assets/arrow.png"])

    assert isinstance(images[0], pygame.Surface)


def test_redrawWindow(monkeypatch):
    class MockScreen:
        def __init__(self):
            self.blit_count = 0

        def blit(self, *args, **kwargs):
            self.blit_count += 1

        def fill(self, color):
            pass

    class MockImage:
        def draw(self, screen):
            screen.blit(None, (0, 0))

    mock_screen = MockScreen()
    monkeypatch.setattr("project.SCREEN", mock_screen)

    mock_image = MockImage()
    redrawWindow(mock_image)

    assert mock_screen.blit_count > 0
