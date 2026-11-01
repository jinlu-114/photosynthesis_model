import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from tabulate import tabulate

df = pd.read_csv("observations_estimated.csv")

# s-curve shape model
def equation_model(t, k, t50):
    return 12 / (1 + np.exp(-k * (t - t50)))

#calculations and fitting of colour
def fit_colour(colour):
    coloured_df = df[df["light"].str.strip() == colour]

    ind_arr = coloured_df["time_min"].to_numpy()
    d_arr = coloured_df["floating_disks"].to_numpy()

    params, covariance = curve_fit(
        equation_model,
        ind_arr,
        d_arr,
        p0=[0.5, 10]
    )

    k, t50 = params

    predictions = equation_model(ind_arr, k, t50)

    rmse = np.sqrt(np.mean((d_arr - predictions) ** 2))

    ss_res = np.sum((d_arr - predictions) ** 2)
    ss_tot = np.sum((d_arr - np.mean(d_arr)) ** 2)

    r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else np.nan

    return ind_arr, d_arr, k, t50, rmse, r_squared

#get curve of one colour
def get_curve(colour):
    ind_arr, d_arr, k, t50, rmse, r_squared = fit_colour(colour)
    
    plt.figure(figsize=(10, 6))

    plt.scatter(ind_arr, d_arr, label=f"Experimental Data of {colour}", color = colour)
    smooth_time = np.linspace(ind_arr.min(), ind_arr.max(), 200)
    predicted_disks = equation_model(smooth_time, k, t50)

    plt.plot(smooth_time, predicted_disks, label="Best-Fit Curve", color = colour)

    #et 50 line
    plt.vlines(
    x=t50,
    ymin=0,
    ymax=equation_model(t50, k, t50),
    colors="red",
    linestyles="dashed",
    label=f"ET50 = {t50:.2f} min"
    )


    print(f"RMSE = {rmse:.2f}")
    print(f"R² = {r_squared:.3f}")
    print(f"k = {k:.3f}")
    print(f"t50 = {t50:.2f} minutes")

    plt.xlabel("Time (minutes)")
    plt.ylabel("Number of Floating Disks")
    plt.title(f"Photosynthesis Under {colour} Light")
    plt.legend()
    plt.show()

#compare curves of multiple colours
def get_curves(colours):
    plt.figure(figsize=(10, 6))
    results = []

    for colour in colours:
        ind_arr, d_arr, k, t50, rmse, r_squared = fit_colour(colour)

        results.append({
        "Light Colour": colour,
        "k": round(k, 3),
        "ET50 (min)": round(t50, 2),
        "RMSE": round(rmse, 3),
        "R²": round(r_squared, 3)
        })

        smooth_time = np.linspace(ind_arr.min(), ind_arr.max(), 200)
        predicted_disks = equation_model(smooth_time, k, t50)

        plt.scatter(ind_arr, d_arr, label=colour, color=colour)

        plt.plot(
            smooth_time,
            predicted_disks,
            color=colour,
            label=f"{colour} (ET50 = {t50:.2f} min)"
        )

        plt.vlines(
        x=t50,
        ymin=0,
        ymax=equation_model(t50, k, t50),
        colors="#ea5c50",
        linestyles="dashed",
        )

    comparison_df = pd.DataFrame(results)
    comparison_df = comparison_df.sort_values("ET50 (min)")

    print(tabulate(
        comparison_df, 
        headers="keys", 
        tablefmt="grid", 
        showindex=False))
    
    comparison_df.to_csv("photosynthesis_comparison.csv", index=False)

    plt.xlabel("Time (minutes)")
    plt.ylabel("Number of Floating Disks")
    plt.title(f"Photosynthesis Under {colours} Light")
    plt.legend()
    plt.show()


get_curve("Red")
get_curves(["Red", "Orange", "Green"])