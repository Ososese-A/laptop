const express = require('express');
const {
    createWorkout,
    getWorkouts,
    getWorkout,
    deleteWorkout,
    updateWorkout
} = require('../controllers/workoutControllers');

const router = express.Router()

//for getting multiple workouts
router.get('/', getWorkouts)

//for getting a single workout
router.get('/:id', getWorkout)

//for adding new workouts
router.post('/', createWorkout)

//delete a workout 
router.delete('/:id', deleteWorkout)

//update a workout
router.patch('/:id', updateWorkout)

module.exports =router