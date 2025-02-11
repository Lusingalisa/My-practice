const express = require('express')
const app = express()

const users=[{name:'Name'}]

app.get('/users',(req, res) =>{
    res.json(users)
})

app.post('/users', (req,res)=>{
    const user = { name: req.body.name, password: req.body}
})
app.listen(3000)