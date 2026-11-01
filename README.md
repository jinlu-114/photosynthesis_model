# Photosynthesis Kinetics Modelling Using Python

A computational biology project that uses nonlinear regression to model photosynthetic activity under different wavelengths of light.

## Overview

Light wavelength influences photosynthetic activity because photosynthetic pigments absorb different wavelengths with varying efficiencies. This project investigates how light colour affects the rate at which leaf disks float during a photosynthesis assay.

Using Python, experimental floating leaf disk data is fitted to a logistic growth model to estimate photosynthetic response kinetics, calculate the time required for 50% of disks to float (ET50), and compare model performance across different light conditions.

## Scientific Background

The floating leaf disk assay is a common method for estimating relative photosynthetic activity. Leaf disks initially sink after air is removed from their internal spaces. During photosynthesis, oxygen accumulates within the disks, increasing their buoyancy and causing them to rise.

By recording the number of floating disks over time, we can approximate the progression of photosynthetic activity under different light conditions.

A lower ET50 generally indicates a faster photosynthetic response under the tested conditions.

## Mathematical Model

The experimental data is fitted to a logistic function:

$ # N(t) = \frac{12}{1 + e^{-k(t - t_{50})}} $

Where:
* N(t) — Predicted number of floating leaf disks at time t
* 12 — Total number of leaf disks in the assay
* k — Logistic growth rate parameter (min⁻¹)
* t50 — Estimated time at which 50% of disks are floating (minutes)

The model parameters are estimated using nonlinear least-squares regression with SciPy's curve_fit().

## Model Evaluation

Two metrics are used to evaluate goodness of fit:

### Root Mean Squared Error (RMSE)

Measures the average magnitude of prediction errors, expressed in floating disks. Lower values indicate a closer fit.

### Coefficient of Determination (R²)

Measures how well the fitted model accounts for variation in the observed floating disk counts. Values closer to 1 generally indicate a better fit.

## Features

* Import and process experimental data from CSV files using Pandas
* Fit logistic growth curves using SciPy
* Estimate ET50 and logistic rate parameters for each light colour
* Calculate RMSE and R² to evaluate model fit
* Visualize experimental observations alongside fitted curves using Matplotlib
* Compare photosynthetic responses across multiple light conditions
* Generate formatted comparison tables using Tabulate
* Export model results to CSV for further analysis

## Results and Visualizations
<img width="1000" height="600" alt="Multiple colour analysis" src="https://github.com/user-attachments/assets/c9696ddd-cd2b-40f8-ba01-c4ebb3e4d70a" />
<img width="1000" height="600" alt="Analysis of Red" src="https://github.com/user-attachments/assets/c47a97cd-3934-4f70-a7dc-ff9bdd28bdd1" />

## Technologies Used
<table>
  <thead>
    <tr>
      <th>Library</th>
      <th>Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Python</td>
      <td>Primary coding language</td>
    </tr>
    <tr>
      <td>Pandas</td>
      <td>Data processing and tabular analysis</td>
    </tr>
    <tr>
      <td>Numpy</td>
      <td>Numerical calculations</td>
    </tr>
    <tr>
      <td>Scipy</td>
      <td>Nonlinear regression and parameter estimation</td>
    </tr>
    <tr>
      <td>Matplotlib</td>
      <td>Scientific data visualization</td>
    </tr>
    <tr>
      <td>Tabulate</td>
      <td>Formatted comparison tables</td>
    </tr>
  </tbody>
</table>

## Project Structure

```
photosynthesis-kinetics/
├── images/
│   ├── comparison.png
│   └── red_fit.png
├── reports/
│   └── photosynthesis_lab_report.pdf
├── photosynthesis.py
├── observations_estimated.csv
├── photosynthesis_comparison.csv
├── requirements.txt
└── README.md
```

The comparison CSV is generated automatically when the multi-colour analysis function runs. File names can be adjusted to match the repository.

## Getting Started
### 1. Clone the repository 
```
git clone <your-repository-url>
cd photosynthesis-kinetics
```

### 2. Install dependencies
```
python3 -m pip install pandas numpy matplotlib scipy tabulate
```

### 3. Prepare dataset
The input CSV should follow this format:
```
light,time_min,floating_disks
Red,0,0
Red,1,0
Red,2,0
Red,3,0
Red,4,1
```

### 4. Run the analysis
The program provides two functions:
```
get_curve("Red")
```
Generates a logistic fit and calculates model statistics for one light condition

```
get_curves(["Red", "Blue", "Green"])
```
Compares multiple light conditions, generates a summary table, and exports the fitted parameters.

Call these functions from the Python script or import them into another Python program.

## Output

The program generates:

1. **Individual light-colour plots:** Experimental observations, fitted logistic curve, and ET50 marker.
2. **Multi-colour comparison plots:** Fitted curves for different light conditions.
3. **Comparison table:** Light colour, logistic rate parameter, ET50, RMSE, and R².
4. **CSV export:** photosynthesis_comparison.csv, containing model results for further analysis.

## Limitations

* The logistic model assumes a maximum of 12 floating disks, matching the assay setup.
* Floating disk counts are an indirect proxy for photosynthetic activity, not direct measurements of oxygen production.
* The fitted model assumes a sigmoidal response and may not describe every experimental condition equally well.
* Model results depend on experimental data quality, sample size, and measurement consistency.
* The current implementation does not estimate confidence intervals or formally test differences between light conditions.

## Project Goal

This project explores how computational modelling can be used to interpret biological experiments. By combining experimental measurements with nonlinear regression and quantitative model evaluation, it aims to demonstrate how mathematical tools can help identify and compare biological response patterns.
