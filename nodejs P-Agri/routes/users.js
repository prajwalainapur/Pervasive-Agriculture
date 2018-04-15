var express = require('express');
var router = express.Router();
var passport = require('passport');
var LocalStrategy = require('passport-local').Strategy;
var values = require('../models/graph_data');
  var fs = require('fs');

var User = require('../models/user');



// Register
router.get('/' , function(req , res){
res.redirect('/users/login');
});

router.get('/register', function(req, res){
	res.render('register');
});

// Login
router.get('/login', function(req, res){
	res.render('login');
});

router.get('/graph', function(req, res){
	res.render('chart');
});

// router.get('/fuelPrices' , function(req, res){
//   res.render('chart');
// });

router.post("/graph", function(req, res){
  values.getdata(function(data){
      var obj = JSON.stringify(data);
      res.send(obj);    
  });
  
});

router.get('/graph', function(req, res){
	res.render('graph' ,  {layout : 'main_layout'});
});

router.get('/index', function(req, res){
	res.render('index' , {layout : 'main_layout'});
});

router.get('/logs', function(req, res){
	res.render('logs' ,  {layout : 'main_layout'});
});

// Register User
router.post('/register' , function(request , response){
		var username = request.body.username;
		var email = request.body.email;
		var password = request.body.password;
		var password2 = request.body.confirm_password;

console.log(username);
console.log(email);
console.log(password);
console.log(password2);
	// request.checkBody('username', 'Name is required').notEmpty();
	request.checkBody('username', 'Username is required').notEmpty();
	request.checkBody('email', 'Email is required').notEmpty();
	request.checkBody('email', 'Email is not valid').isEmail();
	request.checkBody('password', 'Password is required').notEmpty();
	request.checkBody('confirm_password', 'Confirm Password is required').notEmpty();
	request.checkBody('confirm_password', 'Passwords do not match').equals(request.body.password);

var errors = request.validationErrors();
console.log(JSON.stringify(errors));
if(errors){
		response.render('register',{
      errors:errors
});
		
		
	} else {
		console.log("no error");
		var newUser = new User({
		  username: username,
			email:email,
			password: password
});

 		 User.createUser(newUser, function(err, user){
 			if(err) console.log("error here");
      console.log(user); 			
 });

  request.flash('success_msg', 'You are registered and can now login');
  response.redirect('/users/login');
}

});

passport.use(new LocalStrategy(
  function(username, password, done) {
    User.getUserByUsername(username , function(err , user){
      if(err) throw err;
      if(!user){
        return done(null,false,{message : 'Unknown User'});
      }
        User.comparePassword(password , user.password , function(err , isMatch){
      if(isMatch)
        {
            console.log("yes2");

          return done(null,user);
        }
      else
       {
       console.log("no");
        return done(null,false,{message : "Invalid Password"});
      }
      });
    });
  }));

passport.serializeUser(function(user, done) {
  done(null, user.id);
});

passport.deserializeUser(function(id, done) {
  User.getUserById(id, function(err, user) {
    done(err, user);
  });
})

router.post('/login',
  passport.authenticate('local' , {successRedirect:'/users/login' ,faliureRedirect:'/user/register' , failureFlash:true}),
  function(req, res) {
    console.log("yes");
    res.redirect('/users/login');
  });

router.get('/logout', function(request , response){
  request.logout();
  request.flash('success_msg' , 'You are Logged Out');
  response.redirect('/users/login');
});

module.exports = router;

