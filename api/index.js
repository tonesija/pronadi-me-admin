const axios = require('axios')
const DOMAIN = 'http://127.0.0.1:8080'
//spoj na backend server
module.exports = () =>
{
  return axios.create({
    baseURL: DOMAIN,
    crossDomain: true
  })
}
