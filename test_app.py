import pytest
from dash import Dash
import dash.testing.application_runners as app_runner

# Import your Dash app components
from main import lineChart, salesData

# Fixture to set up the app
@pytest.fixture
def app():
    salesData()  # Generate the CSV file if needed
    app = Dash(__name__)
    lineChart()  # Set up the layout of the app
    return app

def test_header_is_present(dash_duo):
    # Start the Dash app
    dash_duo.start_server(app)

    # Check if the header is present with the correct text
    header = dash_duo.find_element("h1")
    assert header is not None
    assert header.text == "Pink Morcel Sales"

def test_visualization_is_present(dash_duo):
    # Start the Dash app
    dash_duo.start_server(app)

    # Check if the graph component is present
    graph = dash_duo.find_element("#pinkMorcel-graph")
    assert graph is not None

def test_region_picker_is_present(dash_duo):
    # Start the Dash app
    dash_duo.start_server(app)

    # Check if the region picker (RadioItems) is present
    radio_items = dash_duo.find_element("#chart-type")
    assert radio_items is not None

    # Verify that the default selected value is "general"
    selected_value = dash_duo.find_element("#chart-type input:checked").get_attribute("value")
    assert selected_value == "general"