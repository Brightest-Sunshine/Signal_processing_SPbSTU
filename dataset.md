# Сбор данных
Представим несколько десятков входных данных для поставленной задачи. Датасет должен быть репрезентативным: покрывать как можно больше возможных типов конфигураций предметов и видов многоугольника.

### 1. Простейший случай
На входе имеем очень большой четырёхугольник и маленький предмет - прищепка

![case1](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/case1.jpg)
Алгоритм должен вернуть YES

### 2. Предельный случай с одним предметом
На входе имеем прямоугольник, который может вплотную поместить в себя пилочку для ногтей. Случай предельный, так как пилочка будет вплотную к краям многоугольника

![case2](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/case2.jpg)
Алгоритм должен вернуть YES

### 3. Простейший случай несоответствия допустимого размера
На входе имеем треугольник и нож, который по габаритам не помещается в фигуру. Случай классифицируем как простейший, так как нож будет выступать за границы фигуры (при параллельном переносе) на достаточное расстояние

![case3](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/case3.jpg)
Алгоритм должен вернуть NO

Теперь рассматриваем всё те же предметы, однако поворачиваем нож на 90 градусов

![case4](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/case4.jpg)
Алгоритм должен вернуть NO

### 4. Предельный случай с двумя предметами
На вход имеем трапецию и два предмета: магнит и прищепку. Рассматриваем несколько предельных случаев, когда от перемещения объектов относительно друг друга, будем получать различные ответы

![case5](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/case5.jpg)
Алгоритм должен вернуть YES

![case6](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/case6.jpg)
Алгоритм должен вернуть NO

![case7](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/case7.jpg)
Алгоритм должен вернуть YES

### 5. Стресс-тест
На вход имеем большой прямоугольник а также весь набор допустимых предметов (в количестве 10 штук).

![case8](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/case8.jpg)
Алгоритм должен вернуть NO

![case9](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/case9.jpg)
Алгоритм должен вернуть YES

### 6. Тесты на некорректные многоугольники
На вход будем получать различные геометрические фигуры, которые не удовлетворяют требованиям задачи.

На вход поступает отрезок

![case10](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/case10.jpg)
Алгоритм должен вернуть NO

На вход поступает точка

![case11](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/case11.jpg)
Алгоритм должен вернуть NO

На вход поступает незамкнутый многоугольник

![case12](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/case12.jpg)
Алгоритм должен вернуть NO

На вход поступает невыпуклый многоугольник

![case13](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/case13.jpg)
Алгоритм должен вернуть NO

### 7. Тест при отсутсвии предметов
На вход поступает многоугольник, но на поверхности не лежит ни одного объекта.

![case18](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/case18.jpg)
Алгоритм должен вернуть YES

### 8. Обычные случаи
Для репрезентативности выборки рассматриваем обычные случаи работы алгоритма, не представляющие собой предельные случаи

![case14](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/case14.jpg)
Алгоритм должен вернуть YES

![case15](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/case15.jpg)
Алгоритм должен вернуть YES

![case16](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/case16.jpg)
Алгоритм должен вернуть YES

![case17](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/case17.jpg)
Алгоритм должен вернуть NO

![case19](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/case19.jpg)
Алгоритм должен вернуть NO

![case20](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/case20.jpg)
Алгоритм должен вернуть NO

![case21](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/case21.jpg)
Алгоритм должен вернуть YES

![case22](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/case22.jpg)
Алгоритм должен вернуть YES

![case23](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/case23.jpg)
Алгоритм должен вернуть NO

![case24](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/case24.jpg)
Алгоритм должен вернуть NO

![case25](https://github.com/Brightest-Sunshine/pictures-for-README-files/blob/master/pics/case25.jpg)
Алгоритм должен вернуть YES
