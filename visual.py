import sqlite3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DATABASE_NAME = "observations.db"


def load_data():
    conn = sqlite3.connect(DATABASE_NAME)

    df = pd.read_sql_query("SELECT * FROM observations", conn)

    conn.close()

    return df


def show_data():
    df = load_data()

    print(df)


def show_first_observations():
    df = load_data()

    print(df.head())


def show_last_observations():
    df = load_data()

    print(df.tail())


def show_columns():
    df = load_data()

    print(df.columns)


def show_data_info():
    df = load_data()

    df.info()


def search_by_target(target):
    df = load_data()

    result = df[df["target"] == target]

    print(result)


def search_by_observer(observer):
    df = load_data()

    result = df[df["observer"] == observer]

    print(result)


def filter_by_exposure(min_exposure):
    df = load_data()

    result = df[df["exposure"] >= min_exposure]

    print(result)


def search_by_observer_and_exposure(observer, min_exposure):
    df = load_data()

    result = df[(df["observer"] == observer) & (df["exposure"] >= min_exposure)]

    print(result)


def sort_by_exposure():
    df = load_data()

    result = df.sort_values(by="exposure")

    print(result)


def show_exposure_sum():
    df = load_data()

    exposure_values = df["exposure"].to_numpy()

    total = np.sum(exposure_values)

    print("Total exposure:", total, "seconds")


def show_exposure_mean():
    df = load_data()

    exposure_values = df["exposure"].to_numpy()

    average = np.mean(exposure_values)

    print("Mean exposure:", average, "seconds")


def equations_observations():
    df = load_data()

    result = df.groupby("observer")["exposure"].agg(["sum", "mean"])

    print(result)


def plot_observations():
    df = load_data()

    plt.bar(df["target"], df["exposure"])

    plt.xlabel("Target")
    plt.ylabel("Exposure (seconds)")
    plt.title("Exposure of Observations")

    plt.show()


def plot_observer_exposure():
    df = load_data()

    result = df.groupby("observer")["exposure"].sum()

    result.plot(kind="bar")

    plt.xlabel("Observer")
    plt.ylabel("Total Exposure")
    plt.title("Observer Exposure")

    plt.show()


def plot_target_exposure():
    df = load_data()

    result = df.groupby("target")["exposure"].sum()

    result.plot(kind="bar")

    plt.xlabel("Target")
    plt.ylabel("Total Exposure")
    plt.title("Target Exposure")

    plt.show()
