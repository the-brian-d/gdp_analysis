
import requests
import pandas as pd


def load_gdp_data():
    """
    Download annual GDP data from the World Bank
    for seven countries between 2000 and 2022.

    Returns
    -------
    pd.DataFrame
        Raw GDP data containing country, year,
        and GDP values.
    """

    countries = "GBR;USA;BRA;JPN;CHN;DEU;CHE"

    indicator = "NY.GDP.MKTP.KD"

    url = (
        f"https://api.worldbank.org/v2/country/"
        f"{countries}/indicator/{indicator}"
    )

    params = {
        "format": "json",
        "date": "2000:2022",
        "per_page": 1000,
    }

    response = requests.get(
        url, params=params, timeout=30
    )
    response.raise_for_status()

    data = response.json()

    if len(data) < 2 or not isinstance(data[1], list):
        raise ValueError("No GDP data returned by the API.")

    df = pd.DataFrame(data[1])

    return df
