# Google Earth Engine

═══════════════════════════════════════════════════════════════════

```
    ██████╗ ███████╗███████╗
   ██╔════╝ ██╔════╝██╔════╝
   ██║  ███╗█████╗  █████╗  
   ██║   ██║██╔══╝  ██╔══╝  
   ╚██████╔╝███████╗███████╗
    ╚═════╝ ╚══════╝╚══════╝
    
    Earth Engine
```

═══════════════════════════════════════════════════════════════════

## About Google Earth Engine

Google Earth Engine combines a multi-petabyte catalog of satellite imagery and geospatial datasets with planetary-scale analysis capabilities.

---

### Key Features

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

- **Planetary-scale analysis** - Process massive datasets
- **Time series analysis** - Track changes over time
- **Machine learning** - Apply ML algorithms at scale
- **Open datasets** - Access petabytes of Earth observation data

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


### Resources

| Resource | Description |
|----------|-------------|
| [Official Website](https://earthengine.google.com/) | Main GEE portal |
| [Code Editor](https://code.earthengine.google.com/) | Web-based IDE |
| [Documentation](https://developers.google.com/earth-engine) | API docs and guides |
| [Data Catalog](https://developers.google.com/earth-engine/datasets) | Available datasets |


════════════════════════════════════════════════════════════════════

### Quick Overview
Google Earth Engine provides **7 dedicated SST datasets** from various sources:
- **NOAA**: OISST (1981-present), CDR WHOI (1988-2021), Pathfinder (1981-2014)
- **JAXA**: GCOM-C/SGLI (3 versions, 2018-present)
- **HYCOM**: Ocean model with 3D temperature (1992-2024)
- **NASA MODIS**: Aqua (2002-2022) and Terra (2000-present) ocean products

*Note: ERA5 reanalysis datasets do not contain sea surface temperature data. VIIRS SST products are not currently available in the GEE catalog.*

═══════════════════════════════════════════════════════════════════

### 1. **NOAA CDR OISST V2.1** (Optimum Interpolation SST)
- **Collection ID**: `NOAA/CDR/OISST/V2_1`
- **Description**: Daily global SST from satellite, ships, and buoys with gap-filling interpolation
- **Spatial Resolution**: 0.25° (approximately 27.8 km)
- **Temporal Resolution**: Daily

```Python
ee.ImageCollection('NOAA/CDR/OISST/V2_1').size().getInfo()
# 16017
```

- **Temporal Coverage**: 1981-09-01 to present

```Python
ee.ImageCollection('NOAA/CDR/OISST/V2_1').sort('system:time_start', True).first().get('system:index').getInfo()
# '19810901'
ee.ImageCollection('NOAA/CDR/OISST/V2_1').sort('system:time_start', False).first().get('system:index').getInfo()
# '20250709'
```

- **Spatial Coverage**: Global
- **Key Bands**: 
  - `sst`: Sea surface temperature
  - `anom`: Temperature anomaly
  - `ice`: Sea ice concentration
  - `err`: Estimated error
- **Notes**: Includes both preliminary (1-day lag) and final (14-day lag) versions

---

### 2. **NOAA CDR SST WHOI V2**
- **Collection ID**: `NOAA/CDR/SST_WHOI/V2`
- **Description**: High-quality Climate Data Record of SST over ice-free oceans
- **Spatial Resolution**: 27.8 km
- **Temporal Resolution**: 3-hourly
- **Temporal Coverage**: 1988-01-01 to 2021-08-31
- **Spatial Coverage**: Global (ice-free oceans)
- **Key Bands**: 
  - `sea_surface_temperature`: SST in Celsius
  - `fill_missing_qc`: Quality control flags
- **Notes**: Uses diurnal variability modeling with AVHRR observations

---

### 3. **GCOM-C/SGLI Sea Surface Temperature**
Three versions available:

#### **V1** (Legacy)
- **Collection ID**: `JAXA/GCOM-C/L3/OCEAN/SST/V1`
- **Temporal Coverage**: 2018-01-01 to 2020-06-28

#### **V2** (Superseded)
- **Collection ID**: `JAXA/GCOM-C/L3/OCEAN/SST/V2`
- **Temporal Coverage**: 2018-01-01 to 2021-11-28

#### **V3** (Current)
- **Collection ID**: `JAXA/GCOM-C/L3/OCEAN/SST/V3`
- **Temporal Coverage**: 2018-01-01 to present (3-4 day latency)

**Common specifications for all versions:**
- **Spatial Resolution**: 4.6 km
- **Temporal Resolution**: Daily
- **Spatial Coverage**: Global
- **Key Bands**: 
  - `SST_AVE`: Average SST
  - Quality flags for day/night observations

---

### 4. **HYCOM Sea Temperature and Salinity**
- **Collection ID**: `HYCOM/sea_temp_salinity`
- **Description**: Data-assimilative hybrid ocean model with 3D temperature data
- **Spatial Resolution**: 0.08° (approximately 8.9 km)
- **Temporal Resolution**: Daily (mostly)

```python
ee.Image(ee.ImageCollection('HYCOM/sea_temp_salinity').sort('system:time_start', True).toList(2).get(0)).get('system:index').getInfo()
# '1992100200'
ee.Image(ee.ImageCollection('HYCOM/sea_temp_salinity').sort('system:time_start', True).toList(2).get(1)).get('system:index').getInfo()
# '1992100300'
ee.Image(ee.ImageCollection('HYCOM/sea_temp_salinity').sort('system:time_start', False).toList(2).get(0)).get('system:index').getInfo()
# '2024090509'
ee.Image(ee.ImageCollection('HYCOM/sea_temp_salinity').sort('system:time_start', False).toList(2).get(1)).get('system:index').getInfo()
# '2024090506'
ee.ImageCollection('HYCOM/sea_temp_salinity').size().getInfo()
# 27098
```

- **Temporal Coverage**: 1992-10-02 to 2024-09-05 (dataset ended)

```python
ee.ImageCollection('HYCOM/sea_temp_salinity').sort('system:time_start', True).first().get('system:index').getInfo()
# '1992100200'
ee.ImageCollection('HYCOM/sea_temp_salinity').sort('system:time_start', False).first().get('system:index').getInfo()
# '2024090509'
```

- **Spatial Coverage**: 80.48°S to 80.48°N

```python
ee.ImageCollection('HYCOM/sea_temp_salinity').sort('system:time_start', False).first().projection().getInfo()
# {'type': 'Projection', 'crs': 'EPSG:4326', 'transform': [0.08, 0, -180.04, 0, -0.04, 90.02]}
```

- **Key Features**: 
  - Temperature at 40 depth levels (0m to 4000m)
  - `water_temp_0` to `water_temp_39` for different depths
  - Also includes salinity data
- **Notes**: Suitable for studying ocean currents and subsurface temperatures

---

### 5. **NASA MODIS-Aqua Ocean Color SMI**
- **Collection ID**: `NASA/OCEANDATA/MODIS-Aqua/L3SMI`
- **Description**: Level 3 ocean color and biology data including SST
- **Spatial Resolution**: 4.6 km
- **Temporal Resolution**: Daily
- **Temporal Coverage**: 2002-07-03 to 2022-02-28 (dataset ended)
- **Spatial Coverage**: Global oceans
- **Key SST Band**: 
  - `sst`: Sea surface temperature
- **Additional Features**: 
  - Chlorophyll-a concentration
  - Remote sensing reflectance
  - Particulate organic carbon
- **Notes**: Aqua satellite data collection ended in early 2022

---

### 6. **NOAA CDR SST Pathfinder V5.3**
- **Collection ID**: `NOAA/CDR/SST_PATHFINDER/V53`
- **Description**: AVHRR-based twice-daily global SST climate data record
- **Spatial Resolution**: 4 km
- **Temporal Resolution**: Twice daily (day/night)
- **Temporal Coverage**: 1981-09-01 to 2014-12-31
- **Spatial Coverage**: Global
- **Key Bands**: 
  - `sea_surface_temperature`: SST in Kelvin * 0.01
  - `dt_analysis`: Difference from reference SST
  - `wind_speed`: Wind speed
  - `sea_ice_fraction`: Sea ice fraction
  - `quality_level`: Quality level (0-5)
- **Notes**: Historical dataset, compliant with GHRSST standards

---

### 7. **NASA MODIS-Terra Ocean Color SMI**
- **Collection ID**: `NASA/OCEANDATA/MODIS-Terra/L3SMI`
- **Description**: Level 3 ocean color and biology data including SST
- **Spatial Resolution**: 4.6 km
- **Temporal Resolution**: Daily
- **Temporal Coverage**: 2000-02-24 to present
- **Spatial Coverage**: Global oceans
- **Key SST Band**: 
  - `sst`: Sea surface temperature
- **Additional Features**: 
  - Chlorophyll-a concentration
  - Remote sensing reflectance
  - Particulate organic carbon
- **Notes**: Terra satellite counterpart to Aqua MODIS

---


════════════════════════════════════════════════════════════════════
