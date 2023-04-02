const mongoose = require('mongoose');

const Schema = mongoose.Schema;
const bookSchema = new Schema({
    name: {
        type: String,
        required: true
    },
    author: {
        type: String,
        required: true
    },
    description: {
        type: String,
        required: true
    },
    pages: {
        type: Number,
        required: true
    },
    status: {
        type: Boolean,
        required: true
    },
    image: {
        type: String,
        required: true
    },

});


module.exports = mongoose.model("Book", bookSchema);