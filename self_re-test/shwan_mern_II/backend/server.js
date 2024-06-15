require('dotenv').config()

const express = require('express');
const mongoose = require('mongoose');
const workoutRoutes = require('./routes/workouts');
const userRoutes = require('./routes/user');

//to create the express app
const app = express();

//middleware
app.use(express.json());

app.use((req, res, next) => {
    console.log(req.path, req.method)
    next()
});

// app.use(workoutRoutes)
app.use('/api/workouts', workoutRoutes);
app.use('/api/user', userRoutes);

    //connect to db
    mongoose.connect(process.env.MONGO_URI)
        .then(()=> {
            //to create teh listener
            app.listen(process.env.PORT, () => {
            console.log('We are connected to the DB and listening from this port', process.env.PORT);
    })
    })
    .catch((error) => {
        console.log(error)
    })