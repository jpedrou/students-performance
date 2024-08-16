import joblib
import pandas as pd
import json
import os

from django.db import transaction
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from time import sleep

from .models import PredictionResults

FILE_PATH = os.path.dirname(__file__)
ROOT_PATH = os.path.join(FILE_PATH, os.pardir)
MODEL_PATH = os.path.join(ROOT_PATH, "modeling/model_pipeline.pickle")


@csrf_exempt
def make_predictions(request):
    sleep(1.5)
    if request.method == "POST":
        body = json.loads(request.body)

        try:

            # User Inputs
            sex = body.get("gender")
            race = body.get("race")
            parental_level_of_education = body.get("parental_level_of_education")
            lunch = body.get("lunch")
            test_preparation_course = body.get("test_preparation_course")
            reading_score = body.get("reading_score")
            writing_score = body.get("writing_score")

            # Load pretrained model
            model_pipeline = joblib.load(MODEL_PATH)

            # Make Prediction
            input_data = pd.DataFrame(
                {
                    "gender": [sex],
                    "race/ethnicity": [race],
                    "parental level of education": [parental_level_of_education],
                    "lunch": [lunch],
                    "test preparation course": [test_preparation_course],
                    "reading score": [reading_score],
                    "writing score": [writing_score],
                }
            )
            prediction = model_pipeline.predict(input_data)
            prediction = round(prediction[0], 2)

            # Saving the data
            with transaction.atomic():
                prediction_results = PredictionResults(
                    sex=sex,
                    race=race,
                    parental_level_of_education=parental_level_of_education,
                    lunch=lunch,
                    test_preparation_course=test_preparation_course,
                    reading_score=reading_score,
                    writing_score=writing_score,
                    math_score_predicton=prediction,
                )
                prediction_results.save()

            return JsonResponse({"success": True, "prediction": prediction})

        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})
