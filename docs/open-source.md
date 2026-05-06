# Open Source Software

The following are selected open source software projects developed or co-developed by Steve Nesbitt and his research group. All projects are hosted on [GitHub](https://github.com/swnesbitt).

---

## Radar & Remote Sensing

### [Py-ART](https://github.com/swnesbitt/pyart)
**Python ARM Radar Toolkit** — A data model driven interactive toolkit for working with weather radar data. Supports reading, processing, visualizing, and writing radar data in a wide variety of formats.

### [xradar](https://github.com/swnesbitt/xradar)
**High-speed Rust port of xradar** — A tool for working with weather radar data in xarray, rewritten with Rust-backed I/O for major performance improvements in radar data ingestion and processing.

### [AWOT](https://github.com/swnesbitt/AWOT)
**Airborne Weather Observations Toolkit** — A Python package for reading, analyzing, and visualizing airborne meteorological and radar data from field campaigns.

### [PyDDA](https://github.com/swnesbitt/PyDDA)
**Pythonic Direct Data Assimilation** — A multiple-Doppler wind retrieval package based on the 3D variational technique. Retrieves 3D wind fields from multiple Doppler radar volumes.

### [CSU_RadarTools](https://github.com/swnesbitt/CSU_RadarTools)
A module of independent functions for doing precipitation retrievals from polarimetric radar data, including hydrometeor classification, rainfall estimation, and retrievals of ice water content.

### [artview](https://github.com/swnesbitt/artview)
**ARM Radar Toolkit Viewer** — An interactive visualization tool for weather radar data built on top of Py-ART.

### [DRpy](https://github.com/swnesbitt/DRpy)
A Python package to open GPM Dual-frequency Precipitation Radar (DPR) files into xarray, enabling use of the full xarray ecosystem for GPM-DPR analysis.

### [radar-data-polygon-viz](https://github.com/swnesbitt/radar-data-polygon-viz)
Demonstration of visualization of weather radar data in its native gate/polygon structure, enabling more accurate spatial representations.

### [open-radar-data](https://github.com/swnesbitt/open-radar-data)
A community repository for sharing radar datasets used across open radar software packages for testing and examples.

---

## Scattering & Microphysics

### [rustmatrix](https://github.com/swnesbitt/rustmatrix)
A Rust-backed T-matrix scattering library for nonspherical particles, ported from pytmatrix with major performance improvements via Rust bindings.

### [Snow-Scattering](https://github.com/swnesbitt/Snow-Scattering)
Simulations of radar backscatter in snowfall, exploring sensitivities to different axial ratios, shapes, densities, and habits.

### [myPSD](https://github.com/swnesbitt/myPSD)
An interactive polarimetric radar particle size distribution (PSD) explorer built with rustmatrix + FastAPI + React.

---

## WRF & Mesoscale Modeling

### [wrf-realtime](https://github.com/swnesbitt/wrf-realtime)
Code to initialize and run WPS and WRF for realtime RELAMPAGO-Argentina forecasts during the 2018–2019 field campaign.

### [mesomodel](https://github.com/swnesbitt/mesomodel)
A collection of code related to mesoscale atmospheric simulation with WRF and CM1.

### [LOFS-read](https://github.com/swnesbitt/LOFS-read)
Code to read, convert, and visualize Leigh Orf's CM1 I/O format (LOFS) for large-eddy simulation output.

### [ARradar](https://github.com/swnesbitt/ARradar)
Python tools to read and analyze data from Argentine weather radars, developed in support of the RELAMPAGO field campaign.

---

## Education & Computing

### [ams-2020-ml-python-course](https://github.com/swnesbitt/ams-2020-ml-python-course)
**Machine Learning in Python for Environmental Science Problems** — Materials for the AMS 2020 Short Course.

### [uiuc-atmos-computing](https://github.com/swnesbitt/uiuc-atmos-computing)
Documentation and tutorials for scientific computing within the Department of Climate, Meteorology & Atmospheric Sciences at the University of Illinois.

### [era5-mcp-server](https://github.com/swnesbitt/era5-mcp-server)
An MCP (Model Context Protocol) server for accessing ERA5 reanalysis data.

### [ipynbhpc](https://github.com/swnesbitt/ipynbhpc)
Utilities for running Jupyter notebooks interactively on HPC (high-performance computing) systems.

### [updraft-forcing](https://huggingface.co/spaces/snesbitt/updraft-forcing)
Interactive Hugging Face Space for exploring updraft forcing in deep convection.

### [mountain-waves](https://huggingface.co/spaces/snesbitt/mountain-waves)
Interactive Hugging Face Space for exploring mountain-wave dynamics.
