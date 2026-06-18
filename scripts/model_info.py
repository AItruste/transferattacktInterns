from deepface import DeepFace

model = DeepFace.build_model("ArcFace")

print(type(model))
print(model.input_shape)
print(model.output_shape)