# extreme-books
ИС для повышения интереса к чтению у студентов (за счет доп. стипендии)


# Инструкции по запуску

## Backend

1. Создаем `.env` файл скопировав `.env_example`
	DATABASE_URL=postgresql+psycopg2://***DB_USER***:***PASSWORD***@localhost:5432/***DB_NAME***
	SECRET=***SECRET_STRING***

2. Создаем `.venv` для Python 
``` bash
python -m venv .venv
```
3. Активируем `.venv` (Windows)
``` bash
.\.venv\Scripts\Activate.ps1
```
4.  Устанавливаем библиотеки для Python
``` shell
pip install -r .\requirements.txt
```
5. Запускаем backend сервер
``` bash
uvicorn app.main:app --reload
```


## Frontend

1. Создаем `.env` файл скопировав `.env_example`
	VUE_APP_SERVER = '***SERVER_IP***:***SERVER_PORT***'

2. Устанавливаем `NVM` и выбираем версию `node` ***ВСТАВИТЬ ВЕРСИЮ***
3. Инизиализируем проект 
``` shell
npm i
```
4. Запускаем проект 
``` shell
npm run serve
```
