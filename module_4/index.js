const express= require("express");
require("dotenv").config()

const db = require('./config');
const app=express()

const port=process.env.PORT || 3000;

app.listen(port,(error)=>{
    console.log(`app is running at ${port}`);
})