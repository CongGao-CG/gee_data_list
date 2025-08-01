#!/usr/bin/env python3
"""
Find missing dates in a Google Earth Engine ImageCollection that should have daily data.

Usage: python find_missing_dates_for_daily_data.py <collection_id>
Example: python find_missing_dates_for_daily_data.py COPERNICUS/MARINE/SATELLITE_OCEAN_COLOR/V6
"""

import ee
import sys
from datetime import datetime


def find_missing_dates_for_daily_data(collection_id):
    """Find missing dates in a daily Earth Engine collection."""
    
    try:
        # Initialize Earth Engine
        ee.Initialize(project='ee-cnggao')
        
        # Get the collection
        collection = ee.ImageCollection(collection_id)
        
        # Check if collection exists and has images
        size = collection.size().getInfo()
        if size == 0:
            print(f"Error: Collection '{collection_id}' is empty or doesn't exist")
            return
        
        print(f"Collection: {collection_id}")
        print(f"Total images in collection: {size}")
        
        # Get date range
        date_range = collection.reduceColumns(
            ee.Reducer.minMax(), ['system:time_start']
        ).getInfo()
        
        start_millis = date_range['min']
        end_millis = date_range['max']
        
        # Create date objects
        start_date = ee.Date(start_millis)
        end_date = ee.Date(end_millis)
        
        # Format dates for display
        start_date_str = start_date.format('YYYY-MM-dd').getInfo()
        end_date_str = end_date.format('YYYY-MM-dd').getInfo()
        
        print(f"Date range: {start_date_str} to {end_date_str}")
        
        # Get number of days
        n_days = end_date.difference(start_date, 'day').add(1).getInfo()
        print(f"Total days in range: {int(n_days)}")
        
        # Create a sequence of all dates
        all_dates = ee.List.sequence(0, n_days - 1).map(
            lambda d: start_date.advance(d, 'day').format('YYYY-MM-dd')
        )
        
        # Get existing dates from the collection
        # First, try to get dates directly from system:time_start
        existing_dates = collection.map(
            lambda img: ee.Feature(None, {
                'date': ee.Date(img.get('system:time_start')).format('YYYY-MM-dd')
            })
        ).aggregate_array('date')
        
        # Find missing dates
        missing = all_dates.removeAll(existing_dates).getInfo()
        
        # Print results
        print(f"\nMissing days: {len(missing)}")
        print(f"Coverage: {(size / n_days * 100):.1f}%")
        
        if len(missing) > 0:
            print("\nMissing dates:")
            
            # Sort missing dates
            missing.sort()
            
            # Group consecutive dates for better display
            if len(missing) <= 50:
                # If not too many, list all dates
                for i, date in enumerate(missing, 1):
                    print(f"  {i:4d}. {date}")
            else:
                # If many missing dates, show first 20, last 20, and summary
                print(f"\nFirst 20 missing dates:")
                for i, date in enumerate(missing[:20], 1):
                    print(f"  {i:4d}. {date}")
                
                print(f"\n  ... ({len(missing) - 40} more dates) ...\n")
                
                print(f"Last 20 missing dates:")
                start_num = len(missing) - 19
                for i, date in enumerate(missing[-20:], start_num):
                    print(f"  {i:4d}. {date}")
                
                # Analyze missing dates by year
                print("\nMissing dates by year:")
                year_counts = {}
                for date in missing:
                    year = date[:4]
                    year_counts[year] = year_counts.get(year, 0) + 1
                
                for year in sorted(year_counts.keys()):
                    print(f"  {year}: {year_counts[year]} days")
        else:
            print("\nNo missing dates found! The collection has complete daily coverage.")
            
    except Exception as e:
        print(f"Error: {str(e)}")
        print("\nMake sure you have:")
        print("1. Installed earthengine-api: pip install earthengine-api")
        print("2. Authenticated with: earthengine authenticate")
        print("3. Provided a valid collection ID")


def main():
    """Main function to handle command line arguments."""
    
    if len(sys.argv) != 2:
        print("Usage: python find_missing_dates_for_daily_data.py <collection_id>")
        print("Example: python find_missing_dates_for_daily_data.py COPERNICUS/MARINE/SATELLITE_OCEAN_COLOR/V6")
        sys.exit(1)
    
    collection_id = sys.argv[1]
    find_missing_dates_for_daily_data(collection_id)


if __name__ == "__main__":
    main()
