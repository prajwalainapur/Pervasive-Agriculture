# Pervasive-Agriculture
Providing Machine Learning and Image Processing to the farmers at just a click of button.

<h2><b>Description:</b></h2><hr/>
The main aim of this project is to help the farmers to earn high revenues at minimal auxillary cost inputs such as fertilizers.

<h2><b>Software/Technical Requirements:</b></h2><hr/>
Flask<br>Open CV for Python<br>Twilio API<br>Google Maps API

<h2> Installation Guide </h2>
<hr/>
<h3> For Python UI 2.0 </h3> <br/>
<ol> 
  <li> Install Flask, Python on your PC. Follow this link if <a href = "http://flask.pocoo.org/docs/0.12/installation/" >required </a> </li>
  <li> Open the directory </li>
  <li> Open command propmt or terminal in that directory </li>
  <li> write "<b><i>python server.py</i></b>" </li>
  <li> Now wait for the message "<i>Running on http://127.0.0.1:8000/</i>" </li>
  <li> Open browser [preferably Chrome] and type "<b>localhost:8000/users/index</b>" and our webapp will open </li>
</ol>
 No need for downloading any other requirements for this<br/>
<h3> For Image Processing </h3> <br/>
<ol>
  <li> Install Python, OpenCV [latest version], NumPy on your PC. </li>
  <li> Open the directory </li>
  <li> OPen command prompt or terminal in that directory </li>
  <li> run "<b><i> python united.py </i></b>" -> The object will be isolated </li>
  <li> run "<b><i> python noise.py </i></b>" -> Required object gets isolated using this script from satellite image </li>
</ol>
<h3> For Alert and Agent System  </h3> <br/>
  <ol>
    <li> Install Python, Flask and Twilio API </li>
    <li> Open the directory </li>
    <li> Open command prompt in the directory </li>
    <li> Download the dependecies using "<b><i>pip install -r requirements.txt</i></b>"</li>
    <li> Run "<b><i>python manage.py runserver</i></b>"</li>
    <li> Open browser and type "<b>localhost:5000/</b>"</li>
</ol>
<h2><b>Services provided:</b></h2><hr/>
The Web application majorly consists of four services, namely
<ul>
<li>    Predictive analysis to suggest the top three more suitable crop based on the nutrition levels of the soil, temperature and also the expected revenue that this particular crop could generate. There are two ways by which this could be used.<br>One would be the automatic way i.e. wherein the farmer just selects their location and based on the previous test that were conducted at or near that place, a suitable crop would be suggested.<br>Second way is to manually enter the details relating to the soil and to obtain a suitable crop for the entered in value.</li>
<li>    A technologiccal base for further development for automated vehicles such as drones and automated tractors. This fundamentaly consists of tha image processing algorithms which are required to plot the routes to traverse the vehicle/drone throughout the field. The image for the same is obtained from Google maps API.</li>
<li>    This feature further suggests the farmers over the substance to be used for the minor deviations that the current soil possess from the ideal requirments. Bio-Fertilizers such as Azotobacter, Pencilium etc... are suggested based on the entered in values.</li>  
<li>    A portal for the farmers where they could send in their query to an agro expert and also contact them fo further details.</li>
</ul>


<h2><b>Implementation Scope:</b></h2><hr/>
This could be implemented at the soil health center provided by the government. Thus, besides meansuring the nutritional values of the sample soil, now they would also provide details regarding the best crop.This would also mean that the product could reach every village in the country where farmers use the soil testing centers.

<h2><b>Developers: </b></h2><hr/>
<ol><li>
Mayank Singh</li>
<li>Prajwal Brijesh Ainapur</li>
<li>Sangamesh Kotalwar</li>
<li>Chaganti Sai Yeshwanth</li>
<li>Athul Khannan
</li></ol>
