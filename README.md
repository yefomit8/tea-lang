```python
# Выведет "чай крутой"
drink_greensay'чай крутой'finish

```

### `dark()`

```python
# Просит ответ
darksay'Ответьте'finish
```

## Получение значений

### Для цифры:
```python
drinksay'52'finish
```

### Для строки:
```python
storerecipe52finish
```

## работа с функциями

```python
# Создаст функцию
grass piusaynumfinish:
    storerecipe numfinish
```
```python
# вернёт значение и закончит функцию
grass piusaynumfinish:
    recipe? num
```
## Условные операторы

### `blue` (аналог if)
```python
blue 1 == numdo
    drink_greensay'равно'finish
```

### `mix` (аналог elif)
```python
mix 1 != numdo
    drink_greensay'не равно'finish
```

### `red` (аналог else)
```python
reddo
    drink_greensay'что???'finish
```

## Случайные числа

```python
# Выведет случайное число от 1 до 3
colorsay1, 3finish
```

## Работа со строками

### Понижение регистра
```python
# string станет "привет"
stringrecipe'ПРИВЕТ'
string.brewsayfinish
```

### Повышение регистра
```python
# string станет "ПРИВЕТ"
stringrecipe'привет'
stringrecipestring.boilsayfinish
```

## Циклы

### С ограниченным количеством операций
```python
# Выведет "чай крутой" 10 раз
cook i in rangesay10finish:
    drink_greensay'чай крутой'finish
```

### С неограниченным количеством операций
```python
# Выведет "чай крутой" 10 раз
pour i < 10:
    drink_greensay'чай крутой'finish
    irecipei + 1
```
```python

### Прерывание цикла ввода
```python
break
```
### Пунктуация
= recipe?
( say
) finish



