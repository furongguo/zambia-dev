# Zambia Development Analysis

Final project for Development Economics: Macro. 
This project analyzes Zambia's and LIC's development patterns using World Bank data.

Topics include:
1. Capital accumulation
2. Demographic structure
3. Economic performance
4. Human capital
5. Inequality
6. Government Role and Performance
7. Geographic and Natural Resource
8. International Linkage

## Project Setup

This project uses uv to manage dependencies. To set up the environment, please install uv package manager and run:

```bash
uv sync
```

## Project Structure

The project is organized into separate directories for data, figures, and analysis to keep the workflow clear and reproducible. 
Files are structured by topic, and the same naming convention is used across folders to maintain consistency. 
You can follow this structure when adding new content or adjust file paths as needed, as long as the data source remains consistent.

```text
.
├── data/
│   ├── LIC_*
│   ├── Zambia_*
├── docs/
├── figures/
│   └── Zambia/
│       ├── capital_accum/
│       ├── demographic/
│       ├── eco_performance/
│       ├── geographic/
│       ├── gov_role/
│       ├── human_capital/
│       ├── inequality/
├── notebooks/
└── src/
```
The description of each directory is as follows:

| Directory    | Description        |
|--------------|--------------------|
| `data/`      | raw datasets       |
| `figures/`   | generated figures  |
| `notebooks/` | .ipynb notebooks   |
| `src/`       | reusable functions |

Please refer to the `notebooks/` directory for detailed analysis and visualizations.
Each notebook corresponds to a specific topic outlined above.
Run the notebooks to generate the figures and insights for Zambia's development analysis.