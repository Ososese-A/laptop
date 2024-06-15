require('dotenv').config()

const express = require('express');
const mongoose = require('mongoose');
const userRoutes = require('./routes/user');

//to create the express app 
const app = express();

//middleware 
app.use(express.json());

//This is for us to know whick routes the client is calling
app.use((req, res, next) => {
    console.log(req.path, req.method)
    next()
});

//This is to register the route with names 
app.use('/api/user', userRoutes);


//this is to connect to the db 
mongoose.connect(process.env.MONGO_URI)
    .then(()=> {
        //the port listener after the DB is connected
        app.listen(process.env.PORT, () => {
            console.log('We are connected to the DB and listenig from this port', process.env.PORT);
        })
    })
    .catch((error) => {
        console.log(error)
    })