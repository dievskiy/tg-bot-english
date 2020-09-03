## Telegram bot

This bot writes english word/idioms with translation on unsplash image based on the data from database and send it to channel.

To start, you need to import or create database. In case of diferent schema, change post_table in schemas/posts.py 

After that:
```
alembic init migratinos
alembic revision --autogenerate -m "create post table"
alembic upgrade head
```
Now, you can run the program:
```
TOKEN_TELEGRAM="XXX" TOKEN_UNSPLASH="XXX" CHANNEL="@channel" python3 main.py
```
Also, you can use crontab or celery for automatic posting

Example channel is [here.](https://t.me/english_idioms_words)