# mpg-lm: a tiny linear model for highway fuel economy

Ordinary least squares model `hwy ~ displ`, fitted on the built-in `mpg` dataset
(`ggplot2`, 234 rows, originally from FuelEconomy.gov).

- `mpg_lm_coefficients.json`: intercept, slope, R-squared and RMSE of the fitted model
- `predict.py`: loads the coefficients and predicts highway mpg from engine displacement (liters)

Usage:

    python predict.py 2.5

License: CC0 1.0 (public domain). Educational demo, not for production forecasting.
