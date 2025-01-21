from fastapi import FastAPI
import pickle
from pydantic import BaseModel

app = FastAPI()

# Загрузка модели
with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)


# Определение модели запроса
class PredictionRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.post("/predict")
def predict(request: PredictionRequest):
    """Make prediction"""

    input_data = [[request.sepal_length, request.sepal_width, request.petal_length, request.petal_width]]
    prediction = model.predict(input_data)

    # Формируем ответ
    return {"prediction": int(prediction[0])}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
