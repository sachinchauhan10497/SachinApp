const express = require('express')
const app = express()
const request = require('request');
const https = require('https')



app.listen(3000, function () {
    console.log('Example app listening on port 3000!')
  })
  
app.get('/sachin', function(req,res){
      url = "localhost:5000"

      request(url, function (response) {
        console.log(url);    
          console.log(response.body);
      });

      res.send("Hii - "+ response.body)
  })