"""
Task 6: Pandas analysis of the Boston Housing dataset.
        Dataset: Boston Housing (https://www.kaggle.com/datasets/altavish/boston-housing-dataset/data)

Subject: IGI
Lab Work: 4
Variant: 3
Version: 1.0
Author: Bibikau M.A.
Date: 20.04.2025
"""

from pathlib import Path

import pandas as pd

import LB3.ui as ui

DATA_PATH = Path(__file__).parent / "HousingData.xls"



def display(obj):
    """Use IPython.display when available, otherwise print."""
    try:
        from IPython.display import display as _d
        _d(obj)
    except ImportError:
        print(obj)



def task_a(df: pd.DataFrame):
    """A. Series и DataFrame — создание, индексирование, display."""

    print("\n" + "═" * 55)
    print("TASK A — Series & DataFrame")
    print("═" * 55)

    # 1. Series из колонки
    print("\n[1] Series — MEDV (первые 8 значений)")
    medv: pd.Series = df["MEDV"]
    display(medv.head(8))
    print(f"dtype: {medv.dtype}  |  size: {medv.size}")

    # 2. Series вручную
    print("\n[2] Series создан вручную (crime_rate по районам)")
    crime_series = pd.Series(
        [0.15, 3.77, 11.58, 0.03, 8.14],
        index=["D1", "D2", "D3", "D4", "D5"],
        name="crime_rate",
    )
    display(crime_series)

    # 3. .loc / .iloc
    print("\n[3] .iloc[1:4]:")
    display(crime_series.iloc[1:4])
    print("\n[3] .loc['D2':'D4']:")
    display(crime_series.loc["D2":"D4"])

    # 4. DataFrame из словаря
    print("\n[4] DataFrame crime_stats из словаря:")
    crime_stats = pd.DataFrame({
        "district":   ["D1", "D2", "D3", "D4", "D5"],
        "crime_rate": [0.15, 3.77, 11.58, 0.03, 8.14],
        "avg_rooms":  [6.2,  5.8,   5.1,  7.4,  4.9],
    })
    display(crime_stats)

    # 5. Основной DataFrame
    print("\n[5] Первые строки датасета Boston Housing:")
    display(df.head())
    print(f"\n    shape: {df.shape}  |  columns: {list(df.columns)}")


def task_b(df: pd.DataFrame):
    """B. Статистический анализ датафрейма."""

    print("\n" + "═" * 55)
    print("  TASK B — Statistical Analysis")
    print("═" * 55)

    # Общая информация
    print("\n[1] df.info():")
    df.info()

    print("\n[1] Пропущенные значения по колонкам:")
    display(df.isnull().sum().rename("missing"))

    print("\n[1] df.describe():")
    display(df.describe().round(3))

    print("\n[1] mean / min / max / std по каждой колонке:")
    display(pd.DataFrame({
        "mean": df.mean(numeric_only=True),
        "min":  df.min(numeric_only=True),
        "max":  df.max(numeric_only=True),
        "std":  df.std(numeric_only=True),
    }).round(4))

    df_clean = df.dropna(subset=["MEDV", "NOX"])

    nox_max = df_clean["NOX"].max()
    nox_min = df_clean["NOX"].min()

    medv_at_max_nox = df_clean.loc[df_clean["NOX"] == nox_max, "MEDV"].mean()
    medv_at_min_nox = df_clean.loc[df_clean["NOX"] == nox_min, "MEDV"].mean()

    ratio = medv_at_max_nox / medv_at_min_nox

    print("\n[2] Средняя цена домов (MEDV) по концентрации оксидов азота (NOX):")
    print(f"    max NOX = {nox_max}  ->  mean MEDV = {medv_at_max_nox:.4f}")
    print(f"    min NOX = {nox_min}  ->  mean MEDV = {medv_at_min_nox:.4f}")
    print(f"\n  Ratio = {ratio:.2f}")

    if ratio < 1:
        print(f"  (при MAX NOX цена в {1/ratio:.2f}x НИЖЕ, чем при MIN NOX)")
    else:
        print(f"  (при MAX NOX цена в {ratio:.2f}x выше)")

    # Дополнительно: корреляционная матрица
    print("\n[3] Топ-5 корреляций с MEDV:")
    corr = df_clean.corr(numeric_only=True)["MEDV"].drop("MEDV").abs().sort_values(ascending=False)
    display(corr.head(5).round(4))


def run():
    """Entry point: load dataset and perform tasks A and B."""

    while True:
        try:
            if not DATA_PATH.exists():
                print(f"\n  [!] File not found: {DATA_PATH}")
                print("  Положите HousingData.xls рядом с task6.py")
                break

            df = pd.read_csv(DATA_PATH)
            df.columns = [c.strip().upper() for c in df.columns]

            task_a(df)
            task_b(df)

        except Exception as exc:
            print(f"Error: {exc}")

        if ui.read_str("\nContinue? (y/n): ").lower() != "y":
            break