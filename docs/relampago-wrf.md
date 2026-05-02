# RELAMPAGO–Argentina WRF Forecasts

<img src="../images/relampago-logo.jpg" alt="RELAMPAGO" style="float: right; width: 130px; margin: 0 0 1rem 1.5rem; border-radius: 6px;">

During the [RELAMPAGO-CACTI field campaign](field-campaigns.md) (2018–2019), the Nesbitt group operated a real-time Weather Research and Forecasting (WRF) model system providing daily convective-scale forecasts over the Córdoba province of Argentina. **Forecasts continue today**, initialized daily from GFS (4 km) and IFS (3 km) initial conditions.

<div style="clear:both;"></div>

## About the Forecasts

The real-time WRF forecasting system was developed and run by Steve Nesbitt's group at the University of Illinois to support operational decision-making during RELAMPAGO field operations. Forecasts were used by scientists and flight crews to identify optimal sampling targets for ground-based and airborne instruments.

- **Model:** WRF-ARW v4.7.1 (Weather Research and Forecasting – Advanced Research WRF)
- **Domain:** Córdoba Province, Argentina and surroundings
- **Horizontal resolution:** 3 km (convection-permitting, no cumulus parameterization)
- **Initial/boundary conditions:** GFS 0.25°, 3-h frequency (campaign); GFS 4 km and IFS 3 km (current operational)
- **Focus:** Convective initiation and evolution in the lee of the Andes

## WRF Configuration

Configuration used during RELAMPAGO-CACTI IOPs, as described in [Casaretto et al. (2022)](https://doi.org/10.1175/WAF-D-21-0006.1):

| Parameter | Value |
|-----------|-------|
| WRF version | 4 |
| Horizontal resolution | 3 km |
| Vertical levels | 51 (user-defined) |
| Model top | 20 hPa |
| Geographic data | MODIS 30 s |
| Projection | Lambert Conformal (32.79°S, 67°W) |
| Microphysics | Thompson (two-moment) |
| Boundary layer | YSU |
| Radiation | RRTMG |
| Land surface | Noah |
| Convection | None (convection-permitting) |

## Code

The initialization and run scripts used for the real-time WRF system are available on GitHub:

[wrf-realtime](https://github.com/swnesbitt/wrf-realtime) — Code to initialize and run WPS and WRF for real-time RELAMPAGO forecasts.

WRF namelist template: [namelist.input](code/namelist.input)

## About RELAMPAGO-CACTI

**RELAMPAGO** (Remote sensing of Electrification, Lightning, And Mesoscale/microscale Processes with Adaptive Ground Observations) was a joint **NSF, DOE, NASA, and NOAA** field campaign. **Steve Nesbitt served as the Lead Principal Investigator of RELAMPAGO** and co-PI of CACTI, coordinating 100+ scientists from 7 agencies across the United States and Argentina. The intensive observing period (IOP) was conducted in Córdoba, Argentina in November–December 2018, with an extended hydrometeorological phase continuing into early 2019. The concurrent **CACTI** campaign (Clouds, Aerosols, and Complex Terrain Interactions), supported by DOE ARM, ran from October 2018 through April 2019.

Science goals included:

- Extreme convective storms in the lee of the Andes
- Orographic forcing of deep convection
- Cloud microphysics and precipitation processes
- Lightning and electrification in subtropical storms

RELAMPAGO-CACTI is the largest land-based field campaign conducted outside the US, with a total budget of **$25M+** across all partner agencies.
