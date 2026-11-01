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

$$
N(t) = \frac{12}{1 + e^{-k(t - t_{50})}}
$$

Where:

N(t) — Predicted number of floating leaf disks at time t

12 — Total number of leaf disks in the assay

k — Logistic growth rate parameter (min⁻¹)

t50 — Estimated time at which 50% of disks are floating (minutes)

The model parameters are estimated using nonlinear least-squares regression with SciPy's curve_fit().
