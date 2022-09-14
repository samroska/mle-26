from models.segmentation import format_input, format_output
import pandas as pd

dataframe = pd.read_json('./test/test_data.json', orient='index')

def test_format_input():
    return_df = format_input(dataframe)
    series_x12 = return_df['x12']
    series_x63 = return_df['x63']

    assert pd.api.types.is_float_dtype(series_x12.dtype)
    assert pd.api.types.is_float_dtype(series_x63.dtype)


