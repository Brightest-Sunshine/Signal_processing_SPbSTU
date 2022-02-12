# Большая лабораторная по курсу "Обработка и интерпретация сигналов" 2022
## Решение задачи с семантическим разрывом

### Выбранные объекты
1. ножницы
2. клей
3. прищепка
4. заколка для волос
5. чайная ложка
6. пилочка для ногтей
7. линейка
8. книжная закладка
9. магнит
10. стикер

### Требования к входным данным
#### для фотографий
- формат изображений Joint Photographic Experts Group (.jpeg, .jpg)
- разрешение фотографий не менее 9.5МП
- отсутствие цветовой коррекции
- отсутствие ретуши
- отсутствие предварительного сжатия
- изображение резкое, без смазанных фрагментов, не шумное
- освещение искусственное, без засвеченных областей и теней по интенсивности сопоставимых с самими объектами
- фотографии сделаны под прямым углом к нормали поверхности с допущением небольшого отклонения до 10°
- многоугольник нарисован на отдельном листе чистой белой бумаги
- линии многоугольника нарисованы чёрным перманентным маркером толщиной 1-3мм

#### для предметов
- толщина объектов не более 2см
- объекты полностью попадают в кадр
- объекты находятся в фокусе
- предметы не должны перекрывать друг друга
- между предметами должен быть зазор не менее 2см
- запрещается появление в кадре двух одинаковых пердметов
- объекты не должны отбрасывать теней
- цвета предметов, присутствующих в кадре, должны быть контрастны относительно друг друга и не сливаться
- цвета предметов, присутствующих в кадре, должна быть контрастны относительно поверхности, на которой располагаются

#### для поверхности
- поверхность должна быть горизонтальная, ровная (не являться выпуклой и/или вогнутой)
- поверхность должна быть достаточного размера, чтобы предметы на ней помещались целиком и не свисали их отдельные части
- поверхность должна быть одной и той же на всех изображениях
- текстура поверхности должна быть однородной и однотонной

#### требования для датасета
- границы предметов должны четко выделяться на фоне белого листа бумаги
- каждый из выбранных предметов на фоне белого листа бумаги А4 должен попадать на фотографию целиком, так чтобы углы и края листа были видны и не перекрывались

### Постановка задачи
На вход поступает фотография, на которой имеется некоторая выборка предметов, ранее выбранных и зафиксированных. Также на фотографии находится белый лист бумаги А4, на котором черным перманентным маркером нарисован многоугольник произвольного размера. 

Необходимо понять, поместятся ли предметы внутрь многоугольника с помощью параллельного переноса.

Объекты могут поместиться в многоугольнике, если при его наложении на совокупность предметов, никакая из сторон объектов не будет выходить за границы фигуры.

### Требование к выходным данным
В качестве ответа на задачу, мы должны в консоли получить один из возможных ответов (бинарная классификация)
- Yes, если предметы поместятся
- No, в противном случае

