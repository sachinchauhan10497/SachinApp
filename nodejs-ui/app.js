console.log("Hello World ! Starting Node.js App...");

const express = require("express");
const bodyParser = require("body-parser");
const request = require("request");
const nl2br  = require("nl2br");

const app = new express();

app.set("view engine", "ejs");
app.set("views", __dirname + "/views");

app.use(express.static(__dirname + "/public"));
app.use(bodyParser.urlencoded({ extended: true }));

const python_api_host = "0.0.0.0";
// const python_api_host = "172.17.0.3";
const python_api_port = "5000";
const get_url = "http://" + python_api_host + ":" + python_api_port + "/" + "?userName=";
const post_url = "http://" + python_api_host + ":" + python_api_port + "?";

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
	request(get_url + userName, function(err, response){
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
				res.render("index", {data: "User Name Dose not exist !"});
			}
		}
	});
});