import pygame
import os
import sys


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()

    image = pygame.image.load(fullname)
    return image


FPS = 50


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    size = width, height = 900, 600
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    intro_text = ['Квадромир', '',
                  'автор Тикшаев Максим']
    logo = load_image('logo.png')
    fon = pygame.transform.scale(load_image('фонменю.png'), (size))
    screen.blit(fon, (0, 0))
    screen.blit(logo, (500, 100))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, False, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
        color = (255, 255, 255)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 20 <= x <= 420 and 200 <= y <= 300:
                    color = (100, 255, 100)
                    return
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if 20 <= x <= 420 and 200 <= y <= 300:
                    color = (100, 255, 100)

                else:
                    color = (255, 255, 255)

        pygame.draw.rect(screen, color, (20, 200, 400, 100), 0)
        pygame.draw.rect(screen, (0, 0, 0), (20, 200, 400, 100), 5)
        text = font.render("Играть", True, (0, 0, 0))
        text_x = 400 // 2 - text.get_width() // 2
        text_y = 500 // 2 - text.get_height() // 2

        screen.blit(text, (text_x, text_y))
        pygame.display.flip()
        clock.tick(50)


def next_level(res):
    if not res:
        with open('data/level.txt', mode='r') as f:
            current_level = int(f.readline().rstrip('\n'))
        with open('data/level.txt', 'w') as g:
            g.write(str(current_level + 1))
    size = width, height = 900, 600
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    intro_text = ['Следующий уровень']
    fon = pygame.transform.scale(load_image('фонменю.png'), (size))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    color = (255, 255, 255)
    color1 = (255, 255, 255)
    for line in intro_text:
        string_rendered = font.render(line, False, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    x, y = 0, 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if 20 <= x <= 420 and 200 <= y <= 300:
                    color = (100, 255, 100)
                else:
                    color = (255, 255, 255)
                if 20 <= x <= 420 and 350 <= y <= 450:
                    color1 = (100, 255, 100)

                else:
                    color1 = (255, 255, 255)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 20 <= x <= 420 and 200 <= y <= 300:
                    color = (100, 255, 100)
                    return
                if 20 <= x <= 420 and 350 <= y <= 450:
                    terminate()

        pygame.draw.rect(screen, color, (20, 200, 400, 100), 0)
        pygame.draw.rect(screen, (0, 0, 0), (20, 200, 400, 100), 5)
        text = font.render("Далее", True, (0, 0, 0))
        text_x = 400 // 2 - text.get_width() // 2
        text_y = 500 // 2 - text.get_height() // 2
        screen.blit(text, (text_x, text_y))

        pygame.draw.rect(screen, color1, (20, 350, 400, 100), 0)
        pygame.draw.rect(screen, (0, 0, 0), (20, 350, 400, 100), 5)
        text1 = font.render("Выход", True, (0, 0, 0))
        text_x1 = 400 // 2 - text.get_width() // 2
        text_y1 = 800 // 2 - text.get_height() // 2
        screen.blit(text1, (text_x1, text_y1))
        pygame.display.flip()
        clock.tick(50)


def end_screen():
    size = width, height = 900, 600
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    intro_text = ['Вы прошли игру', '',
                  'Скоро новый уровень!']
    logo = load_image('cube.png')
    fon = pygame.transform.scale(load_image('фонменю.png'), (size))
    screen.blit(fon, (0, 0))
    screen.blit(logo, (500, 100))
    font = pygame.font.Font(None, 30)
    text_coord = 100
    for line in intro_text:
        string_rendered = font.render(line, False, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
        color = (255, 255, 255)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame.KEYDOWN:
                terminate()
        pygame.display.flip()
        clock.tick(50)


def game_over_screen():
    player = None

    size = width, height = 900, 600
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    intro_text = ['Вы проиграли:(', '']
    logo = load_image('cube.png')
    fon = pygame.transform.scale(load_image('фонменю.png'), (size))
    screen.blit(fon, (0, 0))
    screen.blit(logo, (500, 100))
    font = pygame.font.Font(None, 30)
    text_coord = 100
    color = (255, 255, 255)
    color1 = (255, 255, 255)
    for line in intro_text:
        string_rendered = font.render(line, False, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
        color = (255, 255, 255)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 20 <= x <= 420 and 200 <= y <= 300:
                    terminate()

            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if 20 <= x <= 420 and 200 <= y <= 300:
                    color = (100, 255, 100)

                else:
                    color = (255, 255, 255)

        pygame.draw.rect(screen, color, (20, 200, 400, 100), 0)
        pygame.draw.rect(screen, (0, 0, 0), (20, 200, 400, 100), 5)
        text = font.render("Выход", True, (0, 0, 0))
        text_x = 400 // 2 - text.get_width() // 2
        text_y = 500 // 2 - text.get_height() // 2
        screen.blit(text, (text_x, text_y))

        pygame.display.flip()
        clock.tick(50)


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))
    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


tile_images = {
    'spike': load_image('spike.png'),
    'player': load_image('cube.png'),
    'block': load_image('block.png'),
    'empty': load_image('фон.png'),
    'floor': load_image('низ.png')
}
player_image = load_image('cube.png')

tile_width = tile_height = 100


class Spike(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(enemy_group, all_sprites)
        self.image = tile_images[tile_type]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.mask.get_rect().move(
            tile_width * pos_x, tile_height * pos_y + 50)

    def update(self, key):
        self.rect = self.rect.move(-6, 0)


class Block(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.mask.get_rect().move(
            tile_width * pos_x, tile_height * pos_y + 50)

    def update(self, key):
        self.rect = self.rect.move(-6, 0)


class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(floor_group, all_sprites)
        self.image = tile_images['floor']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.mask.get_rect().move(0, 349)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y + 50)

    def update(self, key):
        if key == 'move':
            self.rect = self.rect.move(0, 0)

    def jump(self, flag, y):
        if flag == False:
            self.rect = self.rect.move(0, 6)
        else:
            self.rect = self.rect.move(0, -6)
        if self.rect.y < y - 200:
            flag = False
            return 'fl'
        if pygame.sprite.spritecollideany(self, floor_group):
            return False
        else:
            return True


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


# основной персонаж
player = None

# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
floor_group = pygame.sprite.Group()


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '*':
                Spike('spike', x, y)
            if level[y][x] == '#':
                Block('block', x, y)
            elif level[y][x] == '@':
                new_player = Player(x, y)
            elif level[y][x] == '.':
                pass
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 10
        self.dy = 10

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - 1200 // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - 500 // 2)


camera = Camera()

background_image = load_image("фон1.png")


def game():
    pygame.init()
    pygame.display.set_caption('Квадромир')
    game_over = False
    with open('data/level.txt', mode='r') as f:
        current_level = int(f.readline().rstrip('\n'))
    if current_level == 1 and not game_over:
        start_screen()
    if current_level == 4:
        end_screen()
    size = width, height = 1200, 500
    screen = pygame.display.set_mode(size)
    player, level_x, level_y = generate_level(load_level(str(current_level) + '.txt'))
    running = True
    clock = pygame.time.Clock()
    x_pos = 0
    floor = Floor()
    is_jump = False
    jump_count = 20
    flag = None
    camera = Camera()
    y = 350
    print(enemy_group)
    while running:
        print(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if pygame.sprite.spritecollideany(player, floor_group) or \
                            pygame.sprite.spritecollideany(player, tiles_group):
                        flag = True
                        is_jump = True
                        y = player.rect.y
        if all([1 if elem.rect.x <= 0 else 0 for elem in enemy_group]) and \
                all([1 if elem1.rect.x <= 0 else 0 for elem1 in tiles_group]):
            running = False
        for elem in tiles_group:
            if player.rect.x + 100 == elem.rect.x and player.rect.y == elem.rect.y:
                game_over_screen()
                return True

        for elem in enemy_group:
            if pygame.sprite.collide_mask(player, elem):
                game_over_screen()
                return True

        if flag == None:
            if not pygame.sprite.spritecollideany(player, tiles_group) and \
                    not pygame.sprite.spritecollideany(player, floor_group):
                flag = False
                is_jump = True

        screen.blit(background_image, (0, 0))
        all_sprites.draw(screen)
        floor.update(screen)
        if is_jump:
            ans = player.jump(flag, y)
            if ans == 'fl':
                flag = False
            else:
                is_jump = ans
            if pygame.sprite.spritecollideany(player, tiles_group):
                is_jump = False
                flag = None
        all_sprites.update('move')
        clock.tick(50)
        pygame.display.flip()


if __name__ == '__main__':
    for i in range(3):
        res = game()
        all_sprites = pygame.sprite.Group()
        with open('data/level.txt', mode='r') as f:
            current_level = int(f.readline().rstrip('\n'))
        if current_level == 3:
            end_screen()
        else:
            next_level(res)
    pygame.quit()
