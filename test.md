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

---

### Quick Start

```javascript
// Initialize the Earth Engine library
var ee = require('@google/earthengine');

// Load a Landsat image
var image = ee.Image('LANDSAT/LC08/C01/T1_TOA/LC08_044034_20140318');

// Display the image
Map.addLayer(image, {bands: ['B4', 'B3', 'B2'], max: 0.3}, 'Landsat 8');
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Resources

| Resource | Description |
|----------|-------------|
| [Official Website](https://earthengine.google.com/) | Main GEE portal |
| [Code Editor](https://code.earthengine.google.com/) | Web-based IDE |
| [Documentation](https://developers.google.com/earth-engine) | API docs and guides |
| [Data Catalog](https://developers.google.com/earth-engine/datasets) | Available datasets |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Logo Placement

> **Note**: To add the official Google Earth Engine logo, download it from the [Google Earth Engine brand resources](https://earthengine.google.com/brand) and place it here using:
> 
> ```markdown
> ![Google Earth Engine Logo](path/to/gee-logo.png)
> ```

════════════════════════════════════════════════════════════════════

---

*Created for Google Earth Engine projects*

════════════════════════════════════════════════════════════════════

---

## Sea Surface Temperature Datasets in Google Earth Engine

Below is a comprehensive list of all sea surface temperature (SST) datasets available in the Google Earth Engine catalog, including their spatial and temporal characteristics.

═══════════════════════════════════════════════════════════════════

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
- **Temporal Coverage**: 1981-09-01 to present
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
- **Temporal Resolution**: Daily
- **Temporal Coverage**: 1992-10-02 to 2024-09-05 (dataset ended)
- **Spatial Coverage**: 80.48°S to 80.48°N
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

### Note on ERA5 Datasets
ERA5 (`ECMWF/ERA5/DAILY`, `ECMWF/ERA5/MONTHLY`) and ERA5-Land datasets focus on atmospheric and land surface parameters. They do **not** contain dedicated sea surface temperature bands. ERA5 provides air temperature, precipitation, and other meteorological variables but not SST specifically.

---

### Key Considerations for SST Data Selection:

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

**1. Resolution Requirements**
- Highest spatial: NOAA Pathfinder (4 km), GCOM-C/SGLI and MODIS (4.6 km)
- Medium spatial: HYCOM (8.9 km)
- Coarse spatial: NOAA OISST, NOAA WHOI (27.8 km)

**2. Temporal Frequency**
- Sub-daily: NOAA CDR WHOI (3-hourly), NOAA Pathfinder (twice daily)
- Daily: Most datasets
- Near real-time: HYCOM (2-day lag in 2024), GCOM-C V3 (3-4 day lag)

**3. Historical Coverage**
- Longest record: NOAA OISST (1981-present), Pathfinder (1981-2014)
- Multi-decadal: HYCOM (1992-2024), NOAA WHOI (1988-2021)
- 2000s onward: MODIS Terra (2000-present), MODIS Aqua (2002-2022)
- Recent: GCOM-C (2018-present)

**4. Special Features**
- 3D ocean data: HYCOM (40 depth levels)
- Quality-controlled climate record: NOAA CDR products
- Ocean biology integration: MODIS-Aqua and Terra L3SMI
- Historical high-resolution: NOAA Pathfinder V5.3

**5. Data Availability Status**
- **Currently Active**: NOAA OISST, GCOM-C V3, MODIS-Terra
- **Recently Ended**: HYCOM (ended Sept 2024), MODIS-Aqua (ended Feb 2022), NOAA WHOI (ended Aug 2021)
- **Historical Only**: NOAA Pathfinder (ended 2014)

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

### Example Code Snippets

```javascript
// 1. Load NOAA OISST data (most commonly used)
var sst = ee.ImageCollection('NOAA/CDR/OISST/V2_1')
  .filterDate('2023-01-01', '2023-12-31')
  .select('sst');

// 2. Load high-resolution MODIS-Aqua SST
var modisSST = ee.ImageCollection('NASA/OCEANDATA/MODIS-Aqua/L3SMI')
  .filterDate('2023-06-01', '2023-06-30')
  .select('sst');

// 3. Load HYCOM for 3D ocean temperature (surface layer)
var hycomSST = ee.ImageCollection('HYCOM/sea_temp_salinity')
  .filterDate('2023-01-01', '2023-01-31')
  .select('water_temp_0')  // Surface temperature
  .map(function(img) {
    return img.multiply(0.001).add(20);  // Scale to Celsius
  });

// Visualize mean SST
var sstVis = {
  min: -2,
  max: 35,
  palette: ['000000', '005aff', '43c8c8', 'fff700', 'ff0000']
};

Map.addLayer(sst.mean(), sstVis, 'NOAA OISST');
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

*Last updated: January 2025*

**Important Notes on Temporal Coverage:**
- Temporal coverage dates were verified as of January 2025
- "Present" indicates the dataset was still being updated at the time of documentation
- Some datasets may have processing delays (e.g., GCOM-C has 3-4 day latency)
- MODIS-Aqua SST appears to have ended in February 2022
- HYCOM data availability in GEE ended in September 2024
- Always check the actual data availability in Google Earth Engine as coverage may change

════════════════════════════════════════════════════════════════════