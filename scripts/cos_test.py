from deepface import DeepFace
import numpy as np

img1 = r"dataset_extractedfaces\lfw_pairs\Renee Zellweger_1.jpg"
img2 = r"dataset_extractedfaces\lfw_pairs\Catherine Deneuve_2.jpg"

e1 = DeepFace.represent(
    img_path=img1,
    model_name="ArcFace",
    detector_backend="skip"
)[0]["embedding"]

e2 = DeepFace.represent(
    img_path=img2,
    model_name="ArcFace",
    detector_backend="skip"
)[0]["embedding"]

e1 = np.array(e1)
e2 = np.array(e2)

sim = np.dot(e1,e2) / (
    np.linalg.norm(e1)*np.linalg.norm(e2)
)

print(sim)