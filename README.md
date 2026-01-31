# BMI Calculator | Калькулятор ИМТ

A full-featured web application for calculating Body Mass Index (BMI).

Полнофункциональное веб-приложение для расчёта индекса массы тела (ИМТ).

## Features | Функции

- **BMI Calculation** - Calculate your Body Mass Index based on weight and height
  (Расчёт индекса массы тела на основе веса и роста)

- **Category Display** - Shows your BMI category (Underweight, Normal, Overweight, Obese)
  (Отображение категории ИМТ: Недостаточный вес, Нормальный, Избыточный, Ожирение)

- **Unit Switching** - Toggle between Metric (kg/cm) and Imperial (lbs/inches) units
  (Переключение между метрической (кг/см) и имперской (фунты/дюймы) системами)

- **History Tracking** - Keeps track of your last 10 BMI calculations
  (Сохранение истории последних 10 расчётов)

- **Bilingual Interface** - English and Russian language support
  (Двуязычный интерфейс: английский и русский)

## Installation | Установка

1. Clone the repository (Клонируйте репозиторий):
```bash
git clone https://github.com/YOUR_USERNAME/bmi-calculator.git
cd bmi-calculator
```

2. Create virtual environment (Создайте виртуальное окружение):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or | или
venv\Scripts\activate  # Windows
```

3. Install dependencies (Установите зависимости):
```bash
pip install -r requirements.txt
```

4. Run the application (Запустите приложение):
```bash
python app.py
```

5. Open in browser (Откройте в браузере):
```
http://localhost:5000
```

## BMI Categories | Категории ИМТ

| BMI Range | Category | Категория |
|-----------|----------|-----------|
| < 18.5 | Underweight | Недостаточный вес |
| 18.5 - 24.9 | Normal weight | Нормальный вес |
| 25 - 29.9 | Overweight | Избыточный вес |
| ≥ 30 | Obese | Ожирение |

## Technologies | Технологии

- Python 3
- Flask
- HTML5 / CSS3
- Jinja2 Templates

## License | Лицензия

MIT License
