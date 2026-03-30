def make_lookup_latex(
    lookup,
    caption,
    label,
    column_format='lp{10cm}'
):
    """
    Create LaTeX code for a World Bank indicator lookup table.

    Example Usage:
    latex_lookup = make_lookup_latex(
    human_cap_lookup,
    caption='World Bank indicators used in Human Capital Analysis',
    label='tab:hc_indicator_list')

    print(latex_lookup)
    """
    return lookup.to_latex(
        index=False,
        escape=True,
        column_format=column_format,
        caption=caption,
        label=label
    )

def make_summary_latex(
    summary,
    caption,
    label,
    drop_series_name=True,
    float_digits=2
):
    """
    Create LaTeX code for a data availability summary table.

    Example Usage:
    latex_summary = make_summary_latex(
    hc_summary,
    caption='Data availability of Human Capital (Zambia)',
    label='tab:hc_data_availability')

    print(latex_summary)
    """
    summary_latex = summary.copy()

    if drop_series_name and 'Series Name' in summary_latex.columns:
        summary_latex = summary_latex.drop(columns=['Series Name'])

    if 'missing_pct' in summary_latex.columns:
        summary_latex['missing_pct'] = summary_latex['missing_pct'].round(1)

    summary_latex = summary_latex.rename(columns={
        'Series Code': 'Series Code',
        'Series Name': 'Series Name',
        'missing_pct': 'Missing (\\%)',
        'n_obs': 'Obs.',
        'first_year': 'First year',
        'last_year': 'Last year'
    })

    return summary_latex.to_latex(
        index=False,
        escape=True,
        float_format=f"%.{float_digits}f",
        caption=caption,
        label=label
    )