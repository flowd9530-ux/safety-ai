# AI-контроль техники безопасности (MVP)

Камера → YOLO → правила нарушений → FastAPI + SQLite → веб-панель.

## Установка
```bash
git clone https://github.com/<твой-ник>/safety-ai.git
cd safety-ai
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Запуск
Будет дополнено на неделе 2.

## Структура
- backend/ — API и база (участник 2)
- detector/ — модель и правила (участники 3, 4)
- frontend/ — панель (участники 5, 6, 7)
- tools/ — генератор событий, замер точности
- config.py — общие настройки

## Договорённости
Будут дополнены в дни 3–4.
