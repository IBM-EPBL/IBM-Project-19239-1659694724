model.predict _proba( [X_test [image_number] . reshape (1, 224,224, 3)])
for idx, result, X in zip ( range (0,6), found, predictions [0)) :
    print(Labe l : if, ype i, Species{}, Score: {}**. format (idx, result [0], result[ll, round (x*100, 3)))
                                                                                      
                                                                                      
#predicting the class with max probability
Class Index=nodel .predict_classes ( [X_test [image_numbe r].reshape (1, 224, 224,3)])
                                                                                      
#getting the index of the class which we can pass
#to the boat_types ist to get the boat type name
Class Index
                                                                                      

#printing the final output
print (found [Class Index [0]])
                                                                                      
#loading Test Data
image_number = np. random. randint (0, len (X_ test))
print(image_number)
                                                                                      
#plotting the test image
plt.figu re ( figsize= (8, 8))
plt.imshow (X_test[image_number])
