import pandas as pd


def clean_gdp_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw GDP data retrieved from the World Bank.

    Parameters
    ----------
    df : pd.DataFrame
        Raw GDP data.

    Returns
    -------
    pd.DataFrame
        Cleaned data containing country, year,
        and GDP values.
    """

    # Work on a copy to preserve the original data
    df = df.copy()

    # Extract country names
    df["country"] = df["country"].apply(
        lambda x: x["value"]
    )

    # Rename columns
    df = df.rename(
        columns={"date": "year", "value": "gdp"}
    )

    # Keep relevant columns
    df = df[["country", "year", "gdp"]]

    # Convert to numeric types
    df["year"] = pd.to_numeric(
        df["year"], errors="coerce"
    )

    df["gdp"] = pd.to_numeric(
        df["gdp"], errors="coerce"
    )

    # Remove observations with missing values
    df = df.dropna(
        subset=["country", "year", "gdp"]
    )

    # Convert year to integer
    df["year"] = df["year"].astype(int)

    # Sort observations
    df = df.sort_values(
        by=["country", "year"]
    )

    # Reset index
    df = df.reset_index(drop=True)

    return df
