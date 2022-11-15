#defining our mo de l, All the laye rs and configu rations
def Load_CNN(Output_size):
K.clear_session 0
model Sequential ()
model.add (D ropout (6.4, input_shape=(224, 224, 3)))
model.add (Conv2D (256, (5, 5),inputshape=(224, 224, 3),activation=' relu"))
model.add (MaxPool2D (pool_size=(2, 2)))
#mode l. add (BatchNo rma lization())
model.add (Conv2D(128, (3, 3), activation=' relu'))
model.add (MaxPool2D (pool_size= (2, 2))
#mode l.add ( BatchNo rma lization ( ))
model.add (Conv2D ( 64, (3, 3), activation=' relu'))
model.add (MaxPool2D (pool_size=(2, 2)))
#model. add (BatchNo rma lization0)
model.add (Flatten ( ))
model.add (Dense (512, activation= " relu '))
model.add (D ropout (0.3))
model.add (Dense (256, activation=" relu' ))
model.ada(Dr0pout(o.3))
model.add (Dense (128, activation=' relu'))
model.add (D ropout (6.3))
model.add (Dense (output _size, activation=' softmax' ))
return modelS
