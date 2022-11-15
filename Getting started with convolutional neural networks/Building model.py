histories_acc=[]
histories_val_acC=[]
histories_loss=[]
histories_val_loss=[]
model.set_weights(weights)
h=mode l.fit(x_train, y_traln,batch_size=16,epochs=7verbose=l,callbacks=[early_stop_loss],shuffle=True,validat1on_data=(X_test, y_test))
model.summary()
