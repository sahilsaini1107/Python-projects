const express = require('express');
const mongoose = require('mongoose');
const router = require("./routes/book_routes");

const app = express();

// middleware

// app.use('/', (req,res,next) => {
//     res.send("Welcome page");
// });

app.use("/books", router);

mongoose
    .connect("mongodb+srv://admin:2bdypDTxc9kKNzwO@cluster0.4hmwqif.mongodb.net/bookstore?retryWrites=true&w=majority")
    .then(()=>console.log('CONNECTED'))
    .then(()=>{
        app.listen(5000);
    }).catch((err)=>console.log(err));

// 2bdypDTxc9kKNzwO