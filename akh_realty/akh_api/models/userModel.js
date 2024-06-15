const mongoose = require('mongoose');
const bcrypt =require('bcrypt');
const validator = require('validator');

const Schema = mongoose.Schema;

const userSchema = new Schema({
    lname: {
        type:String,
        required: true,
    },
    fname: {
        type:String,
        required: true,
    },
    email: {
        type:String,
        required: true,
        unique:true
    },
    mobile: {
        type:String,
        required: true,
        unique:true
    },
    dob: {
        type:String,
        required: true,
    },
    gender: {
        type:String,
        required: true
    },
    address: {
        type:String,
        required: true,
    },
    passportNo: {
        type:String,
        required: true,
        unique:true
    },
    nationality: {
        type:String,
        required: true,
    },
    password: {
        type:String,
        required: true,
        unique:true
    },
    securityQuest: {
        type:String,
        required: true,
    },
    securityAnswer: {
        type: String,
        required: true
    }
})

//this must be a regular function and not an arrow function 
//because it is a static signup method
userSchema.statics.signup = async function (lname, fname, email, mobile, dob, gender, address, passportNo, nationality, password, securityQuest, securityAnswer) {

    //this is to validate the user sign up information
    if (!lname || !fname || !email || !mobile || !dob || !gender || !address || !passportNo || !nationality || !password || !securityQuest || !securityAnswer) {
        throw Error('All fields must be filled')
    }
    if (!validator.isEmail(email)) {
        throw Error('Email is not valid')
    }
    if (!validator.isStrongPassword(password)) {
        throw Error('Passowrd not stong enough')
    }
    //validation ends 

    //checking for uniqueness
    const emailExists = await this.findOne({email})
    const mobileExists = await this.findOne({mobile})
    const passportNoExists = await this.findOne({passportNo})

    if (emailExists) {
        throw Error('Email already in use')
    }

    if (mobileExists) {
        throw Error('Mobile number is already in use')
    }

    if (passportNoExists) {
        throw Error('This passport number is already in use')
    }

    const salt = await bcrypt.genSalt(10)
    const hash = await bcrypt.hash(password, salt)

    const user = await this.create({lname, fname, email, mobile, dob, gender, address, passportNo, nationality, password: hash, securityQuest, securityAnswer})

    return user
}

userSchema.statics.login = async function (email, password) {
    if (!email || !password) {
        throw Error('All fields must be filled')
    }

    const user = await this.findOne({email})

    if (!user) {
        throw Error('Incorrect email')
    }

    const match = await bcrypt.compare(password, user.password)

    if (!match) {
        throw Error('Incorrect password')
    }

    return user
}

module.exports = mongoose.model('User', userSchema)