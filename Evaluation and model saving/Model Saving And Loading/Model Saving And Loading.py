model_json = model.to_json ()                   #indent=-2
with open (" final_model. json", "w") as json_file:
json_tile.write(model_json)

# serialize weights to H5
model.save_weights (" final_model . h5")
print("Saved mode l to di sk")
