import React from "react";
import { Route, Routes } from "react-router-dom";
import Header from "./components/Header";
import Home from "./components/Home";
import AddBook from "./components/AddBook";
import About from "./components/About";



function App() {
  return (
  <React.Fragment>
    <header>
      <Header />
    </header>
    <main>
      <Routes>
        <Route path="/" element={ <Home /> } exact />
        <Route path="/addbook" element={ <AddBook /> } />
        <Route path="/about" element={ <About /> } />
      </Routes>
    </main>
  </React.Fragment>

  );
}

export default App;
