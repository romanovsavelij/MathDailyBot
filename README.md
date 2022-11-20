### Math Daily

This is a Telegram bot with a base of math problems with three different topics and a difficulty setting from 0 to 4 (very easy to insane).
You ask the bot to send a problem by clicking the **"Give task"** button.

The possible commands are:
1. Give task. Before recieving a task there is an option to choose the subject of the problem (Set theory, Logic and Combinatorics)
1. Give a hint (there is one hint for each problem)
2. Give a solution

It is made sure that you don't get the same probem twice.

## Docker

Система состоит из трех компонентов: `PostgreSQL`, бекенда бота и `nginx`. При переходе по адресу `127.0.0.1:1234/images/gopher.png` вы увидете картинку, которую отдает `nginx`. 

Образ с бекендом бота залит в публичный репозиторий [romanovsavelij/math-bot-daily-backend](https://hub.docker.com/r/romanovsavelij/math-bot-daily-backend). 

Запускать так:
```bash
docker-compose up
```
