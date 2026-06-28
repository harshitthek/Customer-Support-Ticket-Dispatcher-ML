from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.prediction_response import PredictionResponse
from model.prediction import predict_output, model, MODEL_VERSION

app = FastAPI()

# human readable       
@app.get('/')
def home():
    return {'message':'Customer Support Ticket Dispatcher'}

# machine readable
@app.get('/health')
def health_check():
    return {
        'status': 'OK',
        'version': MODEL_VERSION,
        'model_loaded': model is not None
    }

@app.post('/predict', response_model=PredictionResponse)
def predict_premium(email: str):
    try:
        prediction = predict_output([email])
        return JSONResponse(status_code=200, content={'response': prediction})
    
    except Exception as e:

        return JSONResponse(status_code=500, content=str(e))