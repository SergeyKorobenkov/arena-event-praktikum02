import pygame
import logic
import surface
import service

SCREEN_DIM = (1180, 675)


pygame.init()
game_display = pygame.display.set_mode(SCREEN_DIM)
pygame.display.set_caption('Arena')


service.service_init()


def create_game(is_new=False):
    global engine, drawer
    if is_new:
        engine = logic.GameEngine()
        drawer = surface.ArenaSurface(
            (1180, 675),
            pygame.SRCALPHA,
            (0, 0),
            surface.ScreenHandle((0, 0))
        )

    drawer.connect_engine(engine)
    service.reload_game(engine)


create_game(True)

while engine.working:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            engine.working = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                engine.working = engine.game_process
                engine.game_process = False
            if engine.game_process:
                if event.key == pygame.K_SPACE:
                    engine.start_fighting()
                if event.key == pygame.K_RETURN:
                    engine.end_fighting()

    game_display.blit(drawer, (0, 0))
    drawer.draw(game_display)
    pygame.display.update()

pygame.display.quit()
pygame.quit()
exit(0)
