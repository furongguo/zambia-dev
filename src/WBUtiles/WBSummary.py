import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def summary_wb(df_clean, lookup, year_col='Year'):
    df = df_clean.set_index(year_col)

    summary = pd.DataFrame({
        'Series Code': df.columns,
        'missing_pct': df.isna().mean().values * 100,
        'n_obs': df.notna().sum().values,
        'first_year': df.apply(lambda s: s.first_valid_index()).values,
        'last_year': df.apply(lambda s: s.last_valid_index()).values,
    })

    summary = summary.merge(
        lookup[['Series Code', 'Series Name']],
        on='Series Code',
        how='left'
    )

    summary = summary[
        ['Series Code', 'Series Name', 'missing_pct', 'n_obs', 'first_year', 'last_year']
    ]

    order = lookup['Series Code'].tolist()
    summary = summary.set_index('Series Code').loc[order].reset_index()

    return summary

def plot_missing_heatmap(
    df_clean,
    year_col='Year',
    lookup=None,
    use_series_name=False,
    figsize=(10, 6),
    xtick_step=5,
    cmap=None
):
    """
    Plot a binary data-availability heatmap.

    Parameters
    ----------
    df_clean : pd.DataFrame
        Clean dataset with one year column and multiple series-code columns.
    year_col : str, default='Year'
        Name of the year column.
    lookup : pd.DataFrame, optional
        Lookup table containing at least:
        - 'Series Code'
        - 'Series Name'
        If provided, the heatmap order will follow lookup order.
    use_series_name : bool, default=False
        If True, show Series Name on the y-axis instead of Series Code.
    figsize : tuple, default=(10, 6)
        Figure size.
    xtick_step : int, default=5
        Step size for x-axis year labels.
    cmap : matplotlib colormap, optional
        Custom colormap. Defaults to binary gray/blue.

    Returns
    -------
    availability : pd.DataFrame
        Binary availability matrix (1=data exists, 0=missing).
    fig, ax : matplotlib Figure and Axes
        Figure and axis objects.
    """

    # build binary availability matrix
    availability = (
        df_clean
        .set_index(year_col)
        .notna()
        .astype(int)
    )

    # align to lookup order if provided
    if lookup is not None:
        order = lookup['Series Code'].tolist()
        availability = availability[order]

    # y-axis labels
    if use_series_name and lookup is not None:
        label_map = lookup.set_index('Series Code')['Series Name'].to_dict()
        ylabels = [label_map.get(c, c) for c in availability.columns]
    else:
        ylabels = availability.columns.tolist()

    # default binary colormap
    if cmap is None:
        cmap = ListedColormap(['#f0f0f0', '#2c7fb8'])  # missing, available

    # plot
    fig, ax = plt.subplots(figsize=figsize)
    ax.imshow(
        availability.T,
        aspect='auto',
        interpolation='nearest',
        cmap=cmap
    )

    ax.set_yticks(range(len(ylabels)))
    ax.set_yticklabels(ylabels)

    xticks = range(0, len(availability.index), xtick_step)
    ax.set_xticks(list(xticks))
    ax.set_xticklabels(availability.index[::xtick_step], rotation=45)

    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel("Series Name" if use_series_name and lookup is not None else "Series Code", fontsize=12)

    ax.grid(False)

    return availability, fig, ax