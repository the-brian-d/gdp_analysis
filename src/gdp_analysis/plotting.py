
import matplotlib.pyplot as plt
import pandas as pd


def plot_gdp(df: pd.DataFrame):
    """
    Plot GDP development for multiple countries.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned GDP data containing country,
        year, and gdp columns.

    Returns
    -------
    matplotlib.figure.Figure
        The GDP line chart.
    """

    fig, ax = plt.subplots(figsize=(12, 7))

    # Plot one line for each country
    for country, group in df.groupby("country"):
        ax.plot(
            group["year"],
            group["gdp"] / 1e12,
            label=country,
            linewidth=2
        )

    ax.set_title(
        "GDP Development (2000–2022)",
        fontsize=16
    )

    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel(
        "Real GDP (trillion constant US$)",
        fontsize=12
    )

    ax.legend(title="Country")
    ax.grid(True, alpha=0.3)

    fig.tight_layout()

    return fig
