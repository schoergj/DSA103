import time

import click
import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)
FORWARD_MODEL_DATA = dict()

# Track API calls for cost simulation
api_call_count = 0
COST_PER_CALL = 0.01  # dollars

@app.route('/predict_forward', methods=['POST'])
def predict_forward():
    """
    Endpoint to predict forward reaction products
    
    Request body:
    {
        "reactants": "CC(=O)O.CCO"  # SMILES string
    }
    
    Response:
    {
        "reactants": "CC(=O)O.CCO",
        "predicted_product": "CC(=O)OCC",
        "confidence": 0.95,
        "call_cost": 0.01
    }
    """

    global api_call_count
    global FORWARD_MODEL_DATA
    
    # Simulate API delay
    time.sleep(0.01)
    
    data = request.get_json()
    reactants = data.get('reactants', '')
    
    api_call_count += 1
    
    # Look up prediction in our mock database
    prediction = {
        "predicted_product": FORWARD_MODEL_DATA.get(reactants, None),
        "confidence": 0.0
    }

    response = {
        "reactants": reactants,
        "predicted_product": prediction.get("predicted_product"),
        "confidence": prediction.get("confidence", 0.0),
        "call_cost": COST_PER_CALL,
        "total_calls": api_call_count
    }

    return response
    

@app.route('/stats', methods=['GET'])
def get_stats():
    """Get API usage statistics"""
    return jsonify({
        "total_calls": api_call_count,
        "total_cost": api_call_count * COST_PER_CALL
    })

@app.route('/reset', methods=['POST'])
def reset_stats():
    """Reset API statistics"""
    global api_call_count
    api_call_count = 0
    return jsonify({"message": "Statistics reset"})

@click.command()
@click.option("--rxn-file", type=click.Path(exists=True), required=True)
def main(rxn_file: str):

    """Main, reads mock reaction data and starts flask server."""

    # Load the forward model predictions from JSON
    global FORWARD_MODEL_DATA
    rxn_fwd = pd.read_json(rxn_file)
    for i in range(len(rxn_fwd)):
        FORWARD_MODEL_DATA[rxn_fwd['reactants'].iloc[i]] = rxn_fwd['predicted_product'].iloc[i]

    print("Starting Mock Forward Model API...")
    print("Available endpoints:")
    print("  POST /predict_forward - Predict forward reaction")
    print("  GET  /stats - Get API usage statistics")
    print("  POST /reset - Reset statistics")
    app.run(debug=True, port=5000)

if __name__ == '__main__':
    main()
