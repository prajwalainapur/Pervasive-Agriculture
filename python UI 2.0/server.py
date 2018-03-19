from flask import Flask , render_template , request , redirect , url_for
app = Flask(__name__)

_code = ""
@app.route("/users/index", methods=["GET","POST"])
def main():
		return render_template('index.html')

@app.route("/users/graph", methods=["GET","POST"])
def login():
		return render_template('chart.html')

@app.route("/users/logs", methods=["GET","POST"])
def logs():
		return render_template('logs.html')

@app.route("/users/analyse", methods=["POST"])
def analyse():
	if(request.method == "POST"):
		import pandas as pd
		import numpy as np
		# import os
		optimum = pd.read_excel("optimum.xlsx", 'Sheet1')
		optimum['N'] = optimum.N.astype(float)
		optimum['P'] = optimum.P.astype(float)
		optimum['K'] = optimum.K.astype(float)
		optimum['TEMPERATURE'] = optimum.TEMPERATURE.astype(float)
		X = optimum.drop("CLASS",axis=1)
		y = optimum.CLASS

		from sklearn.neighbors import KNeighborsClassifier
		clf = KNeighborsClassifier(n_neighbors=1)
		clf.fit(X,y)

		print(request.form.get('Potassium'))
		
		if(request.form.get('Potassium') == None):
			
			pred = pd.read_excel('optimum.xlsx', 'Sheet3')
			
			print(pred)
			prediction = clf.predict(pred)
			print(prediction)
			if(prediction == 7):
				return render_template('crops.html' , crop="TOMATO") 
			elif(prediction == 1):
				return render_template('crops.html' , crop="GARLIC")
			else:
				return "no"
		else:
			potassium = request.form.get('Potassium')
			phosphorous = request.form.get('Phosphorous')
			nitrogen = request.form.get('Nitrogen') 
			pH = request.form.get('pH')
			temperature = request.form.get('Temperature')

			columns = ['N','P','K','pH','TEMPERATURE'] 
			values = np.array([ nitrogen ,phosphorous ,potassium ,   pH , temperature])
			pred = pd.DataFrame(values.reshape(-1, len(values)),columns=columns)
			# print(pred.dtype)
			print(pred)

			prediction = clf.predict(pred)
			print(prediction)
			if(prediction == 7):
				return render_template('crops.html' , crop="TOMATO") 
			elif(prediction == 1):
				return render_template('crops.html' , crop="GARLIC")
			else:
				return "no"


	# render_template('index.html')
	else:
		return render_template('index.html')


		 
		

		
if (__name__ == "__main__"):	
	app.run(host='127.0.0.1', debug=True, port=8000)
