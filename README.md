# ImageWork
Скрипт для сжатия изображений с потерей качества.

Решил попробовать сделать свой настраеваемый метод сжатия изображений с потерями качества.
Суть метода проста кластеризуем полоски изображенния заданной длинный на заданное количество пикселей.
Полученые палитры и координты пикселей сохраняем в сжатом виде.
Конечно такой метод хуже jpg на большинстве картинок.

Пример:

До сжатия png картинка весом 565 кб

![image](https://user-images.githubusercontent.com/72144415/220369446-8548f97d-9123-40b0-a735-3619713efebd.png)


После сжатия получаем 3 файла options, colors, numbers_colors общим весом 150 кб при длинне полоски в 25 пикселей и кластеризацией на 4 цвета.
Полученая картинка весит заметно меньше чем аналогичная в формате png (212 кб) или bmp даже при их сжатии.

![image](https://user-images.githubusercontent.com/72144415/220367438-3f981f5d-a367-4be7-9853-721c684b840c.png)

