import pygame
import os

# Путь к папке с изображениями
assets_dir = os.path.join(os.path.dirname(__file__), 'assets')

# Вывод списка файлов в папке assets для проверки
print("Содержимое папки assets:", os.listdir(assets_dir))

# Размер клетки
CELL_SIZE = 40
SCREEN_EXTRA_HEIGHT = CELL_SIZE  # Высота для таймера и кнопок

# Функция для загрузки и изменения размера изображения
def load_and_scale_image(file_name):
    image = pygame.image.load(os.path.join(assets_dir, file_name))
    return pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))

# Загрузка изображений и изменение их размера
mine_image = load_and_scale_image('mine.gif')
flag_image = load_and_scale_image('flagged.gif')
mine_clicked_image = load_and_scale_image('mineclicked.gif')
misflagged_image = load_and_scale_image('misflagged.gif')

# Загрузка изображений для клеток
blank_image = load_and_scale_image('blank.gif')
open_images = [load_and_scale_image(f'open{i}.gif') for i in range(9)]

# Загрузка изображений для таймера
timer_images = [load_and_scale_image(f'digit{i}.gif') for i in range(10)]

# Загрузка изображений для кнопок смайликов
smiley_image = load_and_scale_image('smiley.gif')
smiley_won_image = load_and_scale_image('smileywon.gif')
smiley_lost_image = load_and_scale_image('smileylost.gif')
