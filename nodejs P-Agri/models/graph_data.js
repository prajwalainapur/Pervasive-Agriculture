var express = require('express');
var mongo = require('mongo');
var mongodb = require('mongodb');
var mongoose = require('mongoose');
var dbHost = "mongodb://localhost:27017/fusion_demo";
 //mongoose.connect('mongodb://localhost/fusion_demo');
 // var db = mongoose.connection;	
app = express();
 var dbObject;
     
    //get instance of MongoClient to establish connection
    var MongoClient = mongodb.MongoClient;
     
    //Connecting to the Mongodb instance.
    //Make sure your mongodb daemon mongod is running on port 27017 on localhost
    MongoClient.connect(dbHost, function(err, db){
      if ( err ) throw err;
      dbObject = db;
    });

//app.get('/' , function(req,res){
module.exports.getdata = function(callback){
getdat(function(err ,  val){
  if(err) throw err;
  else
   callback(val); 
});

};

function getdat(callback){

dbObject.collection("fuel_price").find({}).toArray(function(err, docs){
        if ( err ) throw err;
       
        var monthArray = [];
        var petrolPrices = [];
        var dieselPrices = [];
        var doc,month,petrol;
         
        for ( index in docs){
           doc = docs[index];
          //category array
           month = doc['month'];
          //series 1 values array
           petrol = doc['petrol'];
          //series 2 values array
           diesel = doc['diesel'];
          monthArray.push({"label": month});
          petrolPrices.push({"value" : petrol});
          dieselPrices.push({"value" : diesel});
        }

        var dataset = [
          {
            "seriesname" : "Petrol Price",
            "data" : petrolPrices
          },
          {
            "seriesname" : "Diesel Price",
            "data": dieselPrices
          }
        ];
     
        var response = {
          "dataset" : dataset,
          "categories" : monthArray
        };
      
      //module.exports.mnth = month;
      callback(null , response);
    });

}
