
# coding: utf-8

# In[2]:


from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
numpy.random.seed(7)


# In[20]:


# load pima indians dataset
dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter = ",")
# split into input (X) and output (Y) variables
X = dataset[ :, 0:8 ]
Y = dataset[ :, 8 ]


# In[21]:


# create model
model = Sequential()
model.add( Dense( 12, input_dim = 8, activation = 'relu' ) )
model.add( Dense( 8, activation = 'relu' ) )
model.add( Dense( 1, activation = 'sigmoid' ) )


# In[22]:


# Compile model
model.compile( loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'] )


# In[23]:


# Fit the model
model.fit( X, Y, epochs = 150, batch_size = 10 )


# In[24]:


# evaluate the model
scores = model.evaluate( X, Y )
print( "\n%s: %.2f%%" % ( model.metrics_names[1], scores[1] * 100 ) )


# In[25]:


# Calculate predictions
predictions = model.predict( X )

#round predictions
rounded = [ round( x[0] ) for x in predictions ]
print( rounded )

