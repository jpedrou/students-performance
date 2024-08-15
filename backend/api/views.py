import joblib
import pandas as pd
import json
import os

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from time import sleep

from .models import PredictionResults

FILE_PATH = os.path.dirname(__file__)
ROOT_PATH = os.path.join(FILE_PATH, os.pardir)
MODEL_PATH = os.path.join(ROOT_PATH, "modeling/model_pipeline.pickle")


@csrf_exempt
def make_predictions(request):
    sleep(2)
    if request.method == "POST":
        body = json.loads(request.body)

        try:

            # User Inputs
            sex = body.get("sex")
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

            # # Saving the data
            # prediction_results = PredictionResults()
            # prediction_results.sex = sex
            # prediction_results.race = race
            # prediction_results.parental_level_of_education = parental_level_of_education
            # prediction_results.lunch = lunch
            # prediction_results.test_preparation_course = test_preparation_course
            # prediction_results.reading_score = reading_score
            # prediction_results.writing_score = writing_score
            # prediction_results.math_score_predicton = prediction
            # prediction_results.save()

            return JsonResponse({"success": True, "prediction": prediction})

        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})
