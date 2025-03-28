// src/App.js
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { ChakraProvider } from "@chakra-ui/react";
import Header from "./components/Header";
import MainPage from "./pages/MainPage";
import CategoryPage from "./pages/CategoryPage";
import RankingsPage from "./pages/RankingsPage";

function App() {
  return (
    <ChakraProvider>
      <Router>
        <Routes>
          <Route exact path="/" element={<MainPage />} />
          <Route
            path="/category/:category"
            element={
              <>
                <Header />
                <CategoryPage />
              </>
            }
          />
          <Route
            path="/category/:category/rankings"
            element={
              <>
                <Header />
                <RankingsPage />
              </>
            }
          />
        </Routes>
      </Router>
    </ChakraProvider>
  );
}

export default App;
