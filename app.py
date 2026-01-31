"""
BMI Calculator Web Application
A full-featured BMI calculator with history and unit switching.
"""

from flask import Flask, render_template, request, session, redirect, url_for
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)


def calculate_bmi(weight: float, height: float, unit: str) -> float:
    """Calculate BMI based on weight and height."""
    if unit == 'imperial':
        # Convert pounds to kg and inches to meters
        weight_kg = weight * 0.453592
        height_m = height * 0.0254
    else:
        # Metric: weight in kg, height in cm
        weight_kg = weight
        height_m = height / 100

    if height_m <= 0:
        return 0

    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)


def get_bmi_category(bmi: float) -> dict:
    """Return BMI category with color coding."""
    if bmi < 18.5:
        return {
            'category': 'Underweight',
            'category_ru': 'Недостаточный вес',
            'color': '#3498db',
            'advice': 'Consider consulting a nutritionist to reach a healthy weight.',
            'advice_ru': 'Рекомендуется консультация диетолога для достижения здорового веса.'
        }
    elif bmi < 25:
        return {
            'category': 'Normal weight',
            'category_ru': 'Нормальный вес',
            'color': '#27ae60',
            'advice': 'Great! Maintain your healthy lifestyle.',
            'advice_ru': 'Отлично! Продолжайте вести здоровый образ жизни.'
        }
    elif bmi < 30:
        return {
            'category': 'Overweight',
            'category_ru': 'Избыточный вес',
            'color': '#f39c12',
            'advice': 'Consider increasing physical activity and reviewing your diet.',
            'advice_ru': 'Рекомендуется увеличить физическую активность и пересмотреть рацион.'
        }
    else:
        return {
            'category': 'Obese',
            'category_ru': 'Ожирение',
            'color': '#e74c3c',
            'advice': 'Please consult a healthcare professional for guidance.',
            'advice_ru': 'Рекомендуется обратиться к врачу за консультацией.'
        }


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    unit = session.get('unit', 'metric')

    if 'history' not in session:
        session['history'] = []

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'switch_unit':
            unit = request.form.get('unit', 'metric')
            session['unit'] = unit
        elif action == 'calculate':
            try:
                weight = float(request.form.get('weight', 0))
                height = float(request.form.get('height', 0))
                unit = request.form.get('unit', 'metric')
                session['unit'] = unit

                if weight > 0 and height > 0:
                    bmi = calculate_bmi(weight, height, unit)
                    category_info = get_bmi_category(bmi)

                    result = {
                        'bmi': bmi,
                        'weight': weight,
                        'height': height,
                        'unit': unit,
                        **category_info
                    }

                    # Add to history
                    history_entry = {
                        'date': datetime.now().strftime('%Y-%m-%d %H:%M'),
                        'bmi': bmi,
                        'weight': weight,
                        'height': height,
                        'unit': unit,
                        'category': category_info['category']
                    }

                    history = session.get('history', [])
                    history.insert(0, history_entry)
                    session['history'] = history[:10]  # Keep last 10 entries
                    session.modified = True

            except ValueError:
                result = {'error': 'Please enter valid numbers.'}

        elif action == 'clear_history':
            session['history'] = []
            session.modified = True

    return render_template('index.html',
                         result=result,
                         unit=unit,
                         history=session.get('history', []))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
