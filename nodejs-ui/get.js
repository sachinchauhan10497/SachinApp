const https = require('https')
const options = {
  hostname: 'localhost:5000',
  method: 'GET'
}

const req = https.request(options, res => {
  console.log(`statusCode: ${res.statusCode}`)
})

req.on('error', error => {
  console.error(error)
})

req.end()