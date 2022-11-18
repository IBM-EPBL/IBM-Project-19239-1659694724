# IBM-Project-19239-1659694724

<h1>Project Title:-Digital Naturalist - AI Enabled tool for Biodiversity Researchers</h1>
<h1>Project Id:-PNT2022TMID20816</h1>

<h1>Faculty Mentor(s) Name:- Mathupriya S</h1>  

<h1>Team Members:-</h1>
<ul>
<li>Shanmugapriya P</li>
<li>Dhanushiya Y</li>
<li>Monika B</li>
<li>Aruna A</li>
<li>Sindhumeenal T</li> 
<h2>Domain:-Aritificial Intelligence</h2>

<h2>Project Objective:-</h2>
<h4>A naturalist is someone who studies the patterns of nature, identifies a different kind of flora and fauna in nature.Being able to identify the flora and fauna around us often leads to an interest in protecting wild spaces, and collecting and sharing information about the species we see on our travels is very useful for conservation groups like NCC.

When venturing into the woods, field naturalists usually rely on common approaches like always carrying a guidebook around everywhere or seeking help from experienced ornithologists. There should be a handy tool for them to capture, identify and share the beauty to the outside world. 

Field naturalists can only use this web app from anywhere to identify the birds, flowers, mammals and other species they see on their hikes, canoe trips and other excursions.

In this project, we are creating a web application which uses a deep learning model, trained on different species of birds, flowers and mammals (2 subclasses in each for a quick understanding)and get the prediction of the bird when an image is been given. </h4>

<h2>Architecture Diagram:-</h2>
<img src="https://lh3.googleusercontent.com/zYy7n-JaraSS-1nC47xBKlQVAiGqTda679j8Sg3VgV-VLYAv58JPvHRmn-mcU1O66LTro8pC7eTiUt38RpCX9mSmG4UvQoF7Lp7ZOqJiQ5nqvrZ-G7WVlGv6MPu8FwwB77Q051g"/>
<h2>Project Flow:-</h2>
  <h4><li>Download/Create dataset.</li>
    <li>Augment the dataset</li>
    <li>Preprocess the images and load the data of images into Numpy Arrays.</li>
    <li>Perform a Train Test Split on the dataset.</li>
    <li>Define the model creation function: adding all the neural network layers required.</li>
    <li>Fit the model on train data and check for accuracies using test data as well.</li>
    <li>Save the model and its dependencies.</li></h4>
  <h2>Pre-Requisites</h2>
  In order to develop this project, we need to install the following software/packages

To install Anaconda navigator and to know how to use Jupyter Notebook a Spyder using Anaconda
 
Tensor flow:

 TensorFlow is an end-to-end open-source platform for machine learning. It has a comprehensive, flexible ecosystem of tools, libraries, and community resources that lets researchers push the state-of-the-art in ML and developers can easily build and deploy ML-powered applications.

Keras: 
  
Keras leverages various optimization techniques to make high-level neural network API easier and more performant. 
  
Flask:
  
 Web framework used for building  Web applications
If you are using anaconda navigator, follow the below steps to download the required packages:
Open anaconda prompt.
  <li>Type “pip install numpy” and click enter.</li>
<li>Type “pip install pandas” and click enter.</li>
<li>Type “pip install matplotlib” and click enter.</li>
<li>Type “pip install scikit-learn” and click enter.</li>
<li>Type "pip install tensorflow==1.14.0” and click enter.</li>
<li>Type "pip install keras=2.2.4” and click enter.</li>
<li>Type "pip install opencv-python” and click enter.</li>
<li>Type “pip install Flask” and click enter</li>
