from deepface import DeepFace

img = r"generated_outputs\ArcFace\ATT\adv_r0_Renee_Zellweger_1_to_Catherine_Deneuve_2_impersonation_attack_cc919e7e.png"

emb = DeepFace.represent(
    img_path=img,
    model_name="Facenet512",
    enforce_detection=False
)

print(type(emb))
print(len(emb))

print(len(emb[0]["embedding"]))