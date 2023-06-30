# Conway's Game of Life

![example workflow](https://github.com/daminovvv/game-of-life/actions/workflows/main.yaml/badge.svg)

---
## Описание
Игра в жизнь - клеточный автомат.

---
## Установка

---
### Шаги ДОКЕР
#### Кратко
- [ ] установить docker
- [ ] клонировать репозиторий
- [ ] запустить контейнер
- [ ] перейти по ссылке в браузере


#### 1. Установка Docker
https://docs.docker.com/desktop/install/windows-install/


#### 2. Клонирование репозитория
Создаем папку, заходим в неё, клонируем репозиторий.
```
md game-of-life
cd fgame-of-life
git clone https://github.com/daminovvv/game-of-life.git
```


#### 3. Запуск контейнеров
В папке проекта выполнить:
```
docker compose up --build
```

### 4. Перейти на стартовую страницу

http://127.0.0.1:8000/game-of-life/new_game

### 5. Документацию OpenAPI можно найти на

http://127.0.0.1:8000/docs/