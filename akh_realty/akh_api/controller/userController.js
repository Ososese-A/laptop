const User = require('../models/userModel')
const jwt = require('jsonwebtoken')

const createToken = (_id) => {
    return jwt.sign({_id}, process.env.THE_SECRET, {expiresIn: '1d'})
}

//login a user
const loginUser = async (req, res) => {
    const {email, password} = req.body
    try {
        const user = await User.login(email, password)

        //for creating the session token
        const token = createToken(user._id)

        res.status(200).json({email, token})
    } catch (error) {
        res.status(400).json({error: error,message})
    }
}

//signup a user
const signupUser = async (req, res) => {
    const {lname, fname, email, mobile, dob, gender, address, passportNo, nationality, password, securityQuest, securityAnswer} = req.body

    try {
        const user = await User.signup(lname, fname, email, mobile, dob, gender, address, passportNo, nationality, password, securityQuest, securityAnswer)

        //to create the token
        const token = createToken(user._id)

        res.status(200).json({lname, fname, email, mobile, dob, gender, address, passportNo, nationality, password, securityQuest, securityAnswer, token})
    } catch (error) {
        res.status(400).json({error: error.message, source: "the message is from the controller"})
    }
}

module.exports = {signupUser, loginUser}