import sqlite3
import csv

from observation import observation_from_row

DATABASE_NAME = "observations.db"


def create_table():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS observations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            target TEXT NOT NULL,
            observer TEXT NOT NULL,
            filter_name TEXT NOT NULL,
            exposure REAL NOT NULL,
            wavelength REAL NOT NULL,
            magnitude REAL NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def add_observation(target, observer, filter_name, exposure, wavelength, magnitude):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO observations
        (
            target,
            observer,
            filter_name,
            exposure,
            wavelength,
            magnitude
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """,
        (target, observer, filter_name, exposure, wavelength, magnitude),
    )

    conn.commit()
    conn.close()


def get_all_observations():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            target,
            observer,
            filter_name,
            exposure,
            wavelength,
            magnitude
        FROM observations
    """)

    rows = cursor.fetchall()

    conn.close()

    return [observation_from_row(row) for row in rows]


def search_observation(
    target=None,
    observer=None,
    filter_name=None,
    exposure=None,
    wavelength=None,
    magnitude=None,
):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    query = """
        SELECT
            id,
            target,
            observer,
            filter_name,
            exposure,
            wavelength,
            magnitude
        FROM observations
    """

    conditions = []
    params = []

    if target:
        conditions.append("target = ?")
        params.append(target)

    if observer:
        conditions.append("observer = ?")
        params.append(observer)

    if filter_name:
        conditions.append("filter_name = ?")
        params.append(filter_name)

    if exposure is not None:
        conditions.append("exposure = ?")
        params.append(exposure)

    if wavelength is not None:
        conditions.append("wavelength = ?")
        params.append(wavelength)

    if magnitude is not None:
        conditions.append("magnitude = ?")
        params.append(magnitude)

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    cursor.execute(query, params)

    rows = cursor.fetchall()

    conn.close()

    return [observation_from_row(row) for row in rows]


def delete_observation(observation_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM observations
        WHERE id = ?
        """,
        (observation_id,),
    )

    deleted = cursor.rowcount > 0

    conn.commit()
    conn.close()

    return deleted


def update_observation(
    observation_id,
    target=None,
    observer=None,
    filter_name=None,
    exposure=None,
    wavelength=None,
    magnitude=None,
):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    fields = []
    params = []

    if target:
        fields.append("target = ?")
        params.append(target)

    if observer:
        fields.append("observer = ?")
        params.append(observer)

    if filter_name:
        fields.append("filter_name = ?")
        params.append(filter_name)

    if exposure is not None:
        fields.append("exposure = ?")
        params.append(exposure)

    if wavelength is not None:
        fields.append("wavelength = ?")
        params.append(wavelength)

    if magnitude is not None:
        fields.append("magnitude = ?")
        params.append(magnitude)

    if not fields:
        conn.close()
        return False

    query = "UPDATE observations SET "
    query += ", ".join(fields)
    query += " WHERE id = ?"

    params.append(observation_id)

    cursor.execute(query, params)

    updated = cursor.rowcount > 0

    conn.commit()
    conn.close()

    return updated


def save_to_csv(filename="observations.csv"):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            target,
            observer,
            filter_name,
            exposure,
            wavelength,
            magnitude
        FROM observations
    """)

    rows = cursor.fetchall()

    conn.close()

    with open(filename, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                "id",
                "target",
                "observer",
                "filter_name",
                "exposure",
                "wavelength",
                "magnitude",
            ]
        )

        writer.writerows(rows)

    print("Data exported successfully.")
