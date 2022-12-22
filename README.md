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

Перед запуском надо попросить у [@romanovsavelij](https://t.me/romanovsavelij) файл `key.py` с ключами и добавить его в папку `src/` проект. 
Запускать так:
```bash
docker-compose up
```

## k8s

Запуск k8s через minikube
```bash
minikube start
```

Сборка контейнера бота
```bash
docker build -t math-bot-backend .
```

Пробросим локально собранный образ в minikube
```bash
minikube image load math-bot-backend
```

Создаем deployment базы с volume под нее
```bash
kubectl create -f kube/postgres.yaml
```

Создаем deployment бота
```bash
kubectl create -f kube/app.yaml
```

Открываем доступ изве через LoadBalancer
```bash
kubectl expose deployment math-bot-backend -- type=LoadBalancer ---port=8080
```

Пробросим порт для nginx
```bash
kubectl port-forward math-bot-backend 1234:80
```

Теперь можем посмотреть состояние наше кластера, все должно быть успешно запущено
```bash
minikube dashboard
```

По адресу `http://localhost:1234/images/gopher.png` видим локально гофера, значит все запустилось. 

## ansible

В папке [ansible](https://github.com/romanovsavelij/MathDailyBot/tree/master/ansible) лежат все настройки для ansible. 
В `inventory.hosts` обьявлены хосты, куда мы будем деплоить сервис, в `deploy_playbook.yml` плейбук для деплоя.
В `server/Dockerfile` лежит исходник образа, который запускается на чистой машине, где выкачиваются все нужные зависимости и поднимается сервис. 

Деплоить так:
```bash
ansible-playbook ansible/deploy_playbook.yml -i ansible/inventory.hosts
```

## jenkins

По коммиту запускается jenkins pipeline, который проверяет код и делает деплой на голую продакш машину. 

А запускается по коммиту, прогоняет тесты отдельном контейнере через pytest, отбрасывает результаты тестов в allure, прогоняет анализ кода в Sonar и в конце делает деплой сервиса на продакш хост. 

Нужные для jenkins скрипты лежат [тут](https://github.com/romanovsavelij/MathDailyBot/tree/master/jenkins). \
Пайплайн можно настроить [тут](http://185.151.240.150:8080/job/build/). \
[Sonar](http://185.151.240.150:9000/dashboard?id=sonarqube-mathdailybot) \
[Allure](http://185.151.240.150:8080/job/build/allure/)
