const book = require("../model/book");

const getAllBooks = async (req, res, next) => {
    let books;
    try {
        books = await book.find();
    } catch (err){
        console.log(err);
    }

    if (!books) {
        return res.status(404).json({message:"No books found"});
    }
    return res.status(200).json({ books });
};

exports.getAllBooks = getAllBooks;