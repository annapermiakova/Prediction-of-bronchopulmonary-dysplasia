import streamlit as st
import numpy as np

# Функция для вычисления вероятности с помощью логистической регрессии
def logistic_regression_calculator(X, coefficients, intercept):
    # Calculate logit(p)
    logit_p = intercept
    for i, coef in enumerate(coefficients):
        logit_p += coef * X[i]

    # Calculate probability
    probability = 1 / (1 + np.exp(-logit_p))
    return probability

def main():
    st.title('Neonatal Bot')

    coefficients = [-0.6808858463736446, 0.6762455396834283, -0.6226713869756503, 0.3704844403036638, 0.7862307732878744]
    intercept = 1.1853711415943018

    # Добавление интерфейса взаимодействия с пользователем
    variable = st.selectbox('Выберите переменную', ['Вес при рождении', 'Оценка по шкале Сильвермана', 'Оценка по шкале Апгар', 'Число дней на ИВЛ', 'Доля FiO2'])
    value = st.text_input('Введите значение')

    if st.button('Посчитать'):
        # Создание вектора X в зависимости от введенной переменной
        variable_index = {
            'Вес при рождении': 0,
            'Оценка по шкале Сильвермана': 1,
            'Оценка по шкале Апгар': 2,
            'Число дней на ИВЛ': 3,
            'Доля FiO2': 4
        }
        X_test = [None] * 5
        X_test[variable_index[variable]] = float(value)

        # Вычисление вероятности
        probability = logistic_regression_calculator(X_test, coefficients, intercept)

        # Вывод результата
        st.write(f'Вероятность: {probability * 100:.2f}%')

if __name__ == "__main__":
    main()
