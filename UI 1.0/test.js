  var express = require('express');
  var  passport = require('passport');
  var LocalStrategy = require('passport-local').Strategy;
  var path = require('path');
  var exphbs = require('express-handlebars');
  var expressValidator = require('express-validator');
  var bodyParser = require('body-parser');
  var cookieParser = require('cookie-parser');
  var session = require('express-session');
  var flash = require('connect-flash');
  var mongo = require('mongo');
  var mongoose = require('mongoose');
  var User = require(__dirname + '/models/user');
  mongoose.connect('mongodb://localhost/loginapp');

var db = mongoose.connection;
var app = express();

var users = require('./routes/users');

app.set('views', path.join(__dirname , 'views'));
app.engine('handlebars', exphbs({defaultLayout:'layout'}));
app.set('view engine', 'handlebars');


app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());

 //  app.get('/' , function(request , response){
 //  response.render('login2');
 //  // response.sendFile(path.join(__dirname+'/login2.html'));  
 // });
  
 //  app.get('/user/login' , function(request , response){
 //  response.render('login2');
 //  // response.sendFile(path.join(__dirname+'/login2.html'));  
 // });

 //   app.get('/user/register' , function(request , response){
 //  response.render('register');
 //  // response.sendFile(path.join(__dirname+'/login2.html'));  
 // });
 

app.use(express.static(path.join(__dirname , '/public')));

app.use(session({
    secret: 'secret',
    saveUninitialized: true,
    resave: true
}));

app.use(passport.initialize());
app.use(passport.session());

app.use(expressValidator({
  errorFormatter: function(param, msg, value) {
      var namespace = param.split('.')
      , root    = namespace.shift()
      , formParam = root;

    while(namespace.length) {
      formParam += '[' + namespace.shift() + ']';
    }
    return {
      param : formParam,
      msg   : msg,
      value : value
    };
  }
}));

app.use(flash());

// Global Vars
app.use(function (req, res, next) {
  res.locals.success_msg = req.flash('success_msg');
  res.locals.error_msg = req.flash('error_msg');
  res.locals.error = req.flash('error');
  res.locals.user = req.user || null;
  next();
});

app.use(flash());
app.use(function (req, res, next) {
  res.locals.success_msg = req.flash('success_msg');
  res.locals.error_msg = req.flash('error_msg');
  res.locals.error = req.flash('error');
  res.locals.user = req.user || null;
  next();
});

app.use('/users', users); 


  app.listen(8000);