const express = require('express');

//controller imports
const {signupUser, loginUser} = require('../controller/userController')

const router = express.Router()

//testing get route
router.get('/', (req, res) => {
    res.json({response: "It is still working"})
})

//login route
router.post('/login', loginUser)

//sign up route
router.post('/signup', signupUser)

module.exports = router