"""
Test suite for Pink Morsels Sales Visualizer Dash app.
Tests verify that key components are present and functional using Dash testing framework.
"""

import pytest
from appv1 import app, REGION_OPTIONS, df


def test_header_present():
    """
    Test that the header/title is present in the app.
    Verifies the main title 'Pink Morsels Sales Visualizer' is configured.
    """
    # Get the app layout as a string to inspect components
    layout_str = str(app.layout)
    
    # Verify the title text is present in layout
    assert "Pink Morsels Sales Visualizer" in layout_str, "Header title not found in app layout"
    print("✓ Header test passed: Title is present")


def test_visualization_present():
    """
    Test that the sales chart visualization is present.
    Verifies the graph component with id 'sales-chart' exists.
    """
    # Get the app layout as a string
    layout_str = str(app.layout)
    
    # Verify the graph component with correct ID exists
    assert "sales-chart" in layout_str, "Sales chart component not found in layout"
    
    # Verify it's a dcc.Graph component
    assert "Graph" in layout_str or "graph" in layout_str, "Graph component not configured"
    print("✓ Visualization test passed: Sales chart is present")


def test_region_picker_present():
    """
    Test that the region picker (radio buttons) is present.
    Verifies the radio button group with id 'region-filter' exists
    and contains all expected region options.
    """
    # Get the app layout as a string
    layout_str = str(app.layout)
    
    # Verify the radio button group ID exists
    assert "region-filter" in layout_str, "Region filter component not found in layout"
    
    # Verify RadioItems component is present
    assert "RadioItems" in layout_str or "radioitems" in layout_str.lower(), "RadioItems component not configured"
    
    # Verify all five region options are configured
    assert len(REGION_OPTIONS) == 5, f"Expected 5 region options, found {len(REGION_OPTIONS)}"
    
    # Verify the expected region values
    expected_values = ["all", "north", "east", "south", "west"]
    actual_values = [option["value"] for option in REGION_OPTIONS]
    assert actual_values == expected_values, f"Region options mismatch. Expected {expected_values}, got {actual_values}"
    
    # Verify the expected region labels
    expected_labels = ["All Regions", "North", "East", "South", "West"]
    actual_labels = [option["label"] for option in REGION_OPTIONS]
    assert actual_labels == expected_labels, f"Region labels mismatch. Expected {expected_labels}, got {actual_labels}"
    
    print("✓ Region picker test passed: All 5 region options are present")


def test_app_callback_registered():
    """
    Additional test: Verify that the callback for updating the chart is registered.
    """
    # Check that callbacks are registered in the app
    assert len(app.callback_map) > 0, "No callbacks registered in the app"
    print("✓ Callback test passed: Chart update callback is registered")


def test_data_loaded():
    """
    Additional test: Verify that the CSV data is loaded correctly.
    """
    # Verify dataframe is not empty
    assert not df.empty, "DataFrame is empty - data not loaded"
    
    # Verify required columns exist
    required_columns = ["Date", "Sales", "Region"]
    for col in required_columns:
        assert col in df.columns, f"Required column '{col}' not found in data"
    
    # Verify there's data for all regions
    regions = df["Region"].str.lower().unique()
    expected_regions = ["north", "east", "south", "west"]
    for region in expected_regions:
        assert region in regions, f"Region '{region}' not found in data"
    
    print("✓ Data test passed: CSV data loaded successfully with all regions")
