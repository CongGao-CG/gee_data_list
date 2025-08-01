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
- **Source**: https://www.ncei.noaa.gov/products/optimum-interpolation-sst
- **Collection ID**: `NOAA/CDR/OISST/V2_1`
- **Description**: Daily global SST from satellite, ships, and buoys with gap-filling interpolation
- **Spatial Resolution**: 0.25°

```python
ee.ImageCollection('NOAA/CDR/OISST/V2_1').first().select('sst').projection().nominalScale().getInfo()
# 27829.87269831839
ee.ImageCollection('NOAA/CDR/OISST/V2_1').sort('system:time_start', False).first().projection().getInfo()
# {'type': 'Projection', 'crs': 'EPSG:4326', 'transform': [0.25, 0, -180, 0, -0.25, 90]}
ee.ImageCollection('NOAA/CDR/OISST/V2_1').first().select('sst').getInfo()['bands'][0]['dimensions']
# [1441, 720]
```

- **Temporal Resolution**: Daily

```python
ee.ImageCollection('NOAA/CDR/OISST/V2_1').size().getInfo()
# 16017
d0 = ee.Date.fromYMD(2025, 1, 14)
ee.ImageCollection('NOAA/CDR/OISST/V2_1').filterDate(d0, d0.advance(1, 'day')).size().getInfo()
# 0
# 20250114 is missing
```

- **Temporal Coverage**: 1981-09-01 to present

```python
ee.ImageCollection('NOAA/CDR/OISST/V2_1').sort('system:time_start', True).first().get('system:index').getInfo()
# '19810901'
ee.ImageCollection('NOAA/CDR/OISST/V2_1').sort('system:time_start', False).first().get('system:index').getInfo()
# '20250709'
```

- **Spatial Coverage**: Global

```python
ee.ImageCollection('NOAA/CDR/OISST/V2_1').first().geometry().bounds().getInfo()
# {'type': 'Polygon', 'coordinates': [[[-180, -90], [180, -90], [180, 90], [-180, 90], [-180, -90]]]}
```

- **Key Bands**: 
  - `sst`: Sea surface temperature
  - `anom`: Temperature anomaly
  - `ice`: Sea ice concentration
  - `err`: Estimated error

```python
ee.ImageCollection('NOAA/CDR/OISST/V2_1').first().bandNames().getInfo()
# ['sst', 'anom', 'ice', 'err']
```

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
- **Spatial Resolution**: 0.08°

```python
ee.ImageCollection('HYCOM/sea_temp_salinity').first().select('water_temp_0').projection().nominalScale().getInfo()
# 8905.559807134887
ee.ImageCollection('HYCOM/sea_temp_salinity').sort('system:time_start', False).first().projection().getInfo()
# {'type': 'Projection', 'crs': 'EPSG:4326', 'transform': [0.08, 0, -180.04, 0, -0.04, 90.02]}
ee.ImageCollection('HYCOM/sea_temp_salinity').first().select('water_temp_0').getInfo()['bands'][0]['dimensions']
# [4501, 2001]
```

- **Temporal Resolution**: Daily (mostly)

```python
ee.ImageCollection('HYCOM/sea_temp_salinity').size().getInfo()
# 27098
ee.ImageCollection('HYCOM/sea_temp_salinity').filter(ee.Filter.stringEndsWith('system:index', '00').Not()).sort('system:time_start').aggregate_array('system:index').size().getInfo()
# 15530
ee.ImageCollection('HYCOM/sea_temp_salinity').filter(ee.Filter.stringEndsWith('system:index', '00')).sort('system:time_start').aggregate_array('system:index').size().getInfo()
# 11568
# Found 94 missing dates
d0 = ee.Date.fromYMD(1993, 6, 26)
ee.ImageCollection('HYCOM/sea_temp_salinity').filterDate(d0, d0.advance(1, 'day')).size().getInfo()
# 0
# 19930626 is missing
```

<details>
  <summary>Click to expand</summary>

  94 missing dates

  1. 19930626  
  2. 19941209  
  3. 19960208  
  4. 19960909  
  5. 19960910  
  6. 19960911  
  7. 19960912  
  8. 19960913  
  9. 19960914  
  10. 19960915  
  11. 19960916  
  12. 19960917  
  13. 19960918  
  14. 19960921  
  15. 19960922  
  16. 19960923  
  17. 19960924  
  18. 19960925  
  19. 19960926  
  20. 19960927  
  21. 19960928  
  22. 19960929  
  23. 19960930  
  24. 19961001  
  25. 19961002  
  26. 19961003  
  27. 19961004  
  28. 19961006  
  29. 19961007  
  30. 19961008  
  31. 19961009  
  32. 19961010  
  33. 19961011  
  34. 19961012  
  35. 19961013  
  36. 19961231  
  37. 20000519  
  38. 20000520  
  39. 20000521  
  40. 20010922  
  41. 20130117  
  42. 20130118  
  43. 20130119  
  44. 20130120  
  45. 20130215  
  46. 20130318  
  47. 20130321  
  48. 20130322  
  49. 20130323  
  50. 20130324  
  51. 20130325  
  52. 20130326  
  53. 20130327  
  54. 20130328  
  55. 20130329  
  56. 20130330  
  57. 20130331  
  58. 20130401  
  59. 20130417  
  60. 20130504  
  61. 20130505  
  62. 20130511  
  63. 20130624  
  64. 20130625  
  65. 20130626  
  66. 20130627  
  67. 20130727  
  68. 20130802  
  69. 20131111  
  70. 20140413  
  71. 20150102  
  72. 20150315  
  73. 20150325  
  74. 20150919  
  75. 20160715  
  76. 20160914  
  77. 20160923  
  78. 20161014  
  79. 20161015  
  80. 20161209  
  81. 20170125  
  82. 20170318  
  83. 20170320  
  84. 20170804  
  85. 20170811  
  86. 20170813  
  87. 20170814  
  88. 20170927  
  89. 20171125  
  90. 20180303  
  91. 20180309  
  92. 20180311  
  93. 20180408  
  94. 20180502  

</details>

- **Temporal Coverage**: 1992-10-02 to 2024-09-05 (dataset ended)

```python
ee.ImageCollection('HYCOM/sea_temp_salinity').sort('system:time_start', True).first().get('system:index').getInfo()
# '1992100200'
ee.ImageCollection('HYCOM/sea_temp_salinity').sort('system:time_start', False).first().get('system:index').getInfo()
# '2024090509'
```

- **Spatial Coverage**: Global

```python
ee.ImageCollection('HYCOM/sea_temp_salinity').first().geometry().bounds().getInfo()
# {'type': 'Polygon', 'coordinates': [[[-180, -90], [180, -90], [180, 90], [-180, 90], [-180, -90]]]}
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
