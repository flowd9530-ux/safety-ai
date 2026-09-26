# Как работать с кодом (GitHub Desktop)

## Один раз
1. Зарегистрируйся на github.com, скинь ник архитектору.
2. Прими приглашение в репозиторий (придёт на почту).
3. Установи GitHub Desktop: desktop.github.com, войди в свой аккаунт.
4. File → Clone repository → safety-ai → Clone.

## Каждая новая задача
1. Вверху «Current Branch» → выбери main → нажми Fetch origin, потом Pull origin.
   (Так ты получаешь свежую версию проекта.)
2. «Current Branch» → New Branch → назови имя/задача (например anya/zone) → Create branch.
3. Нажми Publish branch.
4. Работай: Repository → Open in Visual Studio Code. Правь ТОЛЬКО свои файлы.
5. Сохранить работу: в GitHub Desktop слева видны изменения.
   Внизу слева в Summary напиши, что сделал → Commit to имя/задача.
6. Отправить: нажми Push origin.
7. Когда задача готова: Create Pull Request → откроется браузер →
   справа в Reviewers выбери архитектора → Create pull request.
8. Если архитектор попросил исправить: правь, снова Commit и Push. PR обновится сам.

## Нельзя
- Править чужие файлы и config.py, README.md.
- Работать в ветке main.
- Если в GitHub Desktop слева видна папка venv, файлы .pt, .db или видео — не коммить,
  напиши архитектору.

## Что-то пошло не так
Сделай скриншот и отправь архитектору. Ничего не удаляй и не переустанавливай.