# MTS Teta 2026: Airbnb Occupancy Prediction

Ноутбуки для соревнования по прогнозу количества занятых дней объекта недвижимости за год.

Основные файлы:

- `01_contest.ipynb` — полный пайплайн: EDA, feature engineering, обучение базовых моделей, мета-модель, диагностика ошибок и подготовка submission.
- `02_stacking_and_uncertainty.ipynb` — связанное задание по базовому стекингу для регрессии и оценке неопределенности предсказаний через ансамбли моделей.

## Подход

Решение построено как двухуровневый ансамбль. На первом уровне обучаются CatBoost, LightGBM, RandomForest, ExtraTrees, отдельные ветки на interaction-признаках, вероятностные модели для режимов таргета и weighted CatBoost-модели для хвостов распределения.

На втором уровне используется `CatBoostRegressor`, который обучается на OOF-предсказаниях базовых моделей и lookup-признаках по повторяющимся `_id` и похожим объявлениям одного хоста.

В отдельном ноутбуке `02_stacking_and_uncertainty.ipynb` разобрана более базовая версия стекинга и диагностика неопределенности: сравнение отдельных моделей, объединение предсказаний и оценка разброса/ошибки ансамбля.

## Данные

Данные не включены в репозиторий. Для запуска ноутбука нужно локально создать папку `data/` и положить в нее файлы соревнования:

- `train.csv`
- `test.csv`
- `sample_submition.csv`
- `nyc-transit-subway-entrance-and-exit-data.csv`

Файл `sample_submition.csv` нужен только для формирования итогового submission.

Метро-датасет используется для географических признаков. Его можно скачать с Kaggle:

- [NYS NYC Transit Subway Entrance And Exit Data](https://www.kaggle.com/datasets/new-york-state/nys-nyc-transit-subway-entrance-and-exit-data?select=nyc-transit-subway-entrance-and-exit-data.csv)

Также его можно скачать через `kagglehub`:

```python
import kagglehub

path = kagglehub.dataset_download(
    "new-york-state/nys-nyc-transit-subway-entrance-and-exit-data"
)
```

После скачивания файл `nyc-transit-subway-entrance-and-exit-data.csv` нужно положить в папку `data/`.

## Окружение

Проект использует Python `>=3.12`. Зависимости описаны в `pyproject.toml`.

Если используется `uv`:

```bash
uv sync
```

Если используется обычный `pip`, можно установить основные зависимости вручную:

```bash
pip install numpy pandas matplotlib seaborn plotly scikit-learn catboost lightgbm shap jupyter
```

## Запуск

1. Подготовить файлы в `data/`.
2. Открыть нужный ноутбук: `01_contest.ipynb` или `02_stacking_and_uncertainty.ipynb`.
3. Выполнить ячейки сверху вниз.

Итоговые submission-файлы не хранятся в репозитории и локально создаются в папке `submissions/`.
