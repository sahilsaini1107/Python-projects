const express = require('express');
const book = require('../model/Book');
const router = express.Router();
const booksController = require("../controllers/book_controller");


router.get("/", booksController.getAllBooks);
router.post("/", booksController.addBook);
router.get("/:id", booksController.getById);
router.put("/:id", booksController.updateBook);
router.delete("/:id", booksController.deleteBook);




//************* this is also a way but bad design**************

// router.get("/", async (req, res, next) => {
//    //  this route will rpovide all of the books
//     let books;
//     try {
//         books = await book.find();
//     } catch (err){
//         console.log(err);
//     }

//     if (!books) {
//         return res.status(404).json({message:"No books found"});
//     }
//     return res.status(200).json({ books });
// });

// *********************************************************
module.exports = router;
