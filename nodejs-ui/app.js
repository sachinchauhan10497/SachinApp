console.log("Hello World ! Starting Node.js App...");

const express = require("express");
const bodyParser = require("body-parser");
const request = require("request");
const nl2br  = require("nl2br");

const app = new express();

let browserJwtTocken = "null";

app.set("view engine", "ejs");
app.set("views", __dirname + "/views");

app.use(express.static(__dirname + "/public"));
app.use(bodyParser.urlencoded({ extended: true }));

const python_api_host = "0.0.0.0";
// const python_api_host = "172.17.0.3";
const python_api_port = "5000";
const get_url = "http://" + python_api_host + ":" + python_api_port + "/" + "?userName=";
const post_url = "http://" + python_api_host + ":" + python_api_port + "?";
const sign_up_url = "http://" + python_api_host + ":" + python_api_port + "/register?";
const log_in_url = "http://" + python_api_host + ":" + python_api_port + "/login?";

app.listen(3000, () => {
	console.log("Server up!");
});

app.get("/", (req, res) => {
	res.render("home");
});

app.get("/get", (req, res) => {
	res.render("index", {data: null});
});

app.get("/post", (req, res) => {
	res.render("post_index", {output: null});
});

app.post("/post", (req, res) => {
	let userName = req.body.userName;
	let data = req.body.data;
	let url = post_url + "userName=" + userName + "&data=" + encodeURIComponent(data);
	url = url + "&jwt=" + browserJwtTocken;
	console.log(url);
	request.post(url, function(err, response){
		if(err){
			res.render("post_index", {output: "Data Insertion Failed !"});
		}
		else{
			let result = response.body;
			res.render("post_index", {output: "For " + userName + " - " + result});
		}
	});
});

app.post("/get", (req, res) => {
	let userName = req.body.userName;
	let hit_url = get_url + userName + "&jwt=" + browserJwtTocken;
	request(hit_url, function(err, response){
		if(err){
			let result = "Can't Get Data :( ";
			res.render("index", {data: result});
		}
		else{
			let result = response.body;
			if (result !== null && result !== ""){
				res.render("index", {data: result});
			}
			else{
				res.render("index", {data: "User Name - " + userName +" Data not exist !"});
			}
		}
	});
});

app.get("/sign_up", (req, res) => {
	res.render("sign_up_index", {output: "null"});
});

app.post("/sign_up", (req, res) => {
	let userName = req.body.userName;
	let password = req.body.password;
	let url = sign_up_url + "userName=" + userName + "&password=" + password;
	console.log(url);
	request.post(url, function(err, response){
		if(err){
			res.render("sign_up_index", {output: "Sign up Failed !"});
		}
		else{
			let result = response.body;
			res.render("sign_up_index", {output:result});
		}
	});
});

app.get("/log_in", (req, res) => {
	res.render("login_index", {output: "null"});
});

app.post("/log_in", (req, res) => {
	let userName = req.body.userName;
	let password = req.body.password;
	let url = log_in_url + "userName=" + userName + "&password=" + password;
	console.log(url);
	request.get(url, function(err, response){
		if(err){
			res.render("login_index", {output: "Login Failed !"});
		}
		else{
			let result = JSON.parse(response.body);
			console.log(result);
			if (result["response"] == "200"){
				let jwtTocken = result["jwt_tocken"];
				browserJwtTocken = jwtTocken;
				res.render("login_index", {output:"Logged in Successfully !"});
			}
			else{
				res.render("login_index", {output:result["error"]});
			}
		}
	});
});

app.get("/jwt", (req, res) => {
	res.render("jwt", {data: browserJwtTocken});
});

app.get("/logout", (req, res) => {
	browserJwtTocken = "null";
	res.render("jwt", {data: "Logged out !"});
});