# Гистограммная атака на СГ-НЗБ

## Необходимое ПО:

- Git - [Скачать и установить Git](https://git-scm.com/downloads).
- Python3 - [Скачать и установить Python](https://www.python.org/downloads/).

## Как скачать и запустить приложение:

### 1. Склонировать репозиторий:
```
git clone https://github.com/dumbus/histogramAttack.git
```
### 2. Перейти в директорию проекта:
```
cd histogramAttack
```
### 3. Установить необходимые библиотеки:

```
pip install Pillow
```

```
pip install opencv-python
```

```
pip install matplotlib
```

### 4. Запустить приложение:

```
python main.py
```

## Подготовка исходных данных:

Для работы программы в одной директории с файлом `main.py` должны содержаться папки с изображениями, для которых будет проводиться атака:

* Названия папок: `imgs-<название изображения>`

* Названия изображений:
- ПО: `<название изображения>.<PNG | JPEG | PPM | GIF | TIFF | BMP>`
- СО с долей вложения 1: `<название изображения>100%.<PNG | JPEG | PPM | GIF | TIFF | BMP>`
- СО с долей вложения 0,5: `<название изображения>50%.<PNG | JPEG | PPM | GIF | TIFF | BMP>`
- СО с долей вложения 0,1: `<название изображения>100%.<PNG | JPEG | PPM | GIF | TIFF | BMP>`
- СО с долей вложения 0,01: `<название изображения>100%.<PNG | JPEG | PPM | GIF | TIFF | BMP>`

Пример корректных данных: <изображение>

## Пример работы программы:

Программа будет выводить матрицу яркостей и гистограмму для каждой отдельной картинки по очереди.

Пример матрицы яркостей: <изображение>

Пример гистограммы: <изображение>

После закрытия окна с гистограммой выведутся данные для следующей в очереди картинки.