#!/usr/bin/env python
"""Access one month of ERA-5 data from Google Cloud, subset over the
northeast US, keep pressure levels >= 600 hPa, and pull u/v wind,
specific humidity, temperature, and geopotential.

Data source: the public Analysis-Ready, Cloud-Optimized (ARCO) ERA5
Zarr store hosted by Google Cloud (no credentials required):

    gs://gcp-public-data-arco-era5/ar/full_37-1h-0p25deg-chunk-1.zarr-v3

Requirements:
    pip install xarray zarr gcsfs dask netcdf4

Reference:
    Carver & Merose (2023), ARCO-ERA5,
    https://github.com/google-research/arco-era5
"""

import xarray as xr

# ----------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------
ARCO_ERA5 = "gs://gcp-public-data-arco-era5/ar/full_37-1h-0p25deg-chunk-1.zarr-v3"

# Month to grab (inclusive start, exclusive end is handled by slice).
YEAR = 2021
MONTH = 1

# Northeast US bounding box (degrees).
LAT_MIN, LAT_MAX = 37.0, 47.5
LON_MIN, LON_MAX = -82.0, -66.0  # roughly Ohio Valley to the Atlantic coast

# Lowest pressure level to keep. "Pressures >= 600 hPa" means the lower
# troposphere: 600, 650, 700, 750, 775, 800, 825, 850, 875, 900, 925,
# 950, 975, 1000 hPa.
MIN_PRESSURE_HPA = 600

# Variables of interest (ARCO-ERA5 names).
VARIABLES = [
    "u_component_of_wind",
    "v_component_of_wind",
    "specific_humidity",
    "temperature",
    "geopotential",
]

OUTPUT = f"era5_northeast_us_{YEAR}{MONTH:02d}.nc"


def main():
    # Open the cloud Zarr store lazily (chunked, nothing downloaded yet).
    ds = xr.open_zarr(ARCO_ERA5, chunks={"time": 48}, consolidated=True)

    # Select the variables we want.
    ds = ds[VARIABLES]

    # --- Time: one month --------------------------------------------------
    start = f"{YEAR}-{MONTH:02d}-01"
    end_month = MONTH + 1 if MONTH < 12 else 1
    end_year = YEAR if MONTH < 12 else YEAR + 1
    end = f"{end_year}-{end_month:02d}-01"
    ds = ds.sel(time=slice(start, end))

    # --- Vertical: pressure levels >= 600 hPa -----------------------------
    ds = ds.sel(level=ds.level >= MIN_PRESSURE_HPA)

    # --- Horizontal: northeast US -----------------------------------------
    # ERA5 longitudes run 0..360, so convert the western box accordingly.
    lon_min = LON_MIN % 360
    lon_max = LON_MAX % 360
    # ERA5 latitude is stored north-to-south (descending), so slice high->low.
    ds = ds.sel(
        latitude=slice(LAT_MAX, LAT_MIN),
        longitude=slice(lon_min, lon_max),
    )

    print(ds)

    # Trigger the download/compute and write to a local netCDF file.
    print(f"\nWriting subset to {OUTPUT} ...")
    ds.to_netcdf(OUTPUT)
    print("Done.")


if __name__ == "__main__":
    main()
