import dash
from dash import html, dcc

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('PhotoGUI Webapp'),
    html.P('Welcome to the Dash version of PhotoGUI.'),
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select a Data File')
        ]),
        style={
            'width': '100%', 'height': '60px', 'lineHeight': '60px',
            'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px',
            'textAlign': 'center', 'margin': '10px'
        },
        multiple=False
    ),
    html.Div(id='upload-status', style={'margin': '10px', 'color': 'red'}),
    html.Label('Baseline (s):'),
    dcc.Input(id='baseline', type='number', value=10),
    html.Label('Snip Length (s):'),
    dcc.Input(id='snip-length', type='number', value=30),
    html.Label('Snip Frequency (Hz):'),
    dcc.Input(id='snip-freq', type='number', value=10),
    html.Label('Noise Threshold:'),
    dcc.Input(id='noise-thresh', type='number', value=10),
    html.Button('Process Data', id='process-btn', n_clicks=0),
    html.Div(id='process-status', style={'margin': '10px', 'color': 'green'}),
    dcc.Store(id='session-data'),
])


# Dash callback setup
from dash.dependencies import Input, Output, State
import base64
import io
from photogui_webapp.utils.data_processing import processdata, time2samples, mastersnipper
import numpy as np

@app.callback(
    Output('upload-status', 'children'),
    Output('session-data', 'data'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename')
)
def handle_file_upload(contents, filename):
    if contents is None:
        return '', None
    try:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        # For now, just store the raw bytes and filename
        file_data = {
            'filename': filename,
            'raw_bytes': content_string
        }
        status = f"Loaded file: {filename}"
        return status, file_data
    except Exception as e:
        return f"Error loading file: {str(e)}", None


# Callback to process data when button is clicked
@app.callback(
    Output('process-status', 'children'),
    Input('process-btn', 'n_clicks'),
    State('session-data', 'data'),
    State('baseline', 'value'),
    State('snip-length', 'value'),
    State('snip-freq', 'value'),
    State('noise-thresh', 'value')
)
def process_data_callback(n_clicks, session_data, baseline, snip_length, snip_freq, noise_thresh):
    if n_clicks == 0 or session_data is None:
        return ''
    try:
        # Example: decode file and run dummy processing
        raw_bytes = session_data['raw_bytes']
        decoded = base64.b64decode(raw_bytes)
        # Here you would parse the file into numpy arrays, etc.
        # For demonstration, just create dummy arrays
        data = np.random.randn(1000)
        datauv = np.random.randn(1000)
        fs = 100
        # Run processing functions (replace with real parsing)
        datafilt = processdata(data, datauv, normalize=True)
        t2sMap = time2samples(data, fs)
        snips = mastersnipper(data, datauv, datafilt, fs, [10, 20, 30], snipfs=snip_freq, preTrial=baseline, trialLength=snip_length, threshold=noise_thresh)
        return f"Data processed! Snips shape: {np.array(snips['snips']).shape}"
    except Exception as e:
        return f"Error processing data: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
