import os
os.environ["TF_USE_LEGACY_KERAS"] = "1"
import kagglehub
import tensorflow_text as text
import tf_keras as keras
import tensorflow_hub as hub
import tensorflow as tf
import numpy as np
import json

MODEL_VERSION = '1.0.0'
path = kagglehub.model_download("pernavjain/customer-support-dispatcher/keras/default")
print("Path to model files:", path)
model = keras.models.load_model(
    f"{path}/customer_support_ticket_dispatcher_v1.keras",
    custom_objects={"KerasLayer": hub.KerasLayer},
    compile=False
)

def predict_output(email:list):
	prediction = model.predict(email)
	team_probs = tf.nn.softmax(prediction[0][0], axis=-1).numpy()
	predicted_class = np.argmax(team_probs)
	urgency_score = prediction[1][0][0]
	with open(f"{path}/id_to_team.json") as f:
		id_to_team = json.load(f)
	predicted_team = id_to_team[f"{predicted_class}"]
	confidence = team_probs[predicted_class]
	return {
		'predicted_team' : predicted_team,
		'confidence' : float(confidence),
		'urgency_score' : float(urgency_score)
	}