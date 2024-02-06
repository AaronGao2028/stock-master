import FinancialForm from "./components/Form/FinancialForm";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import { VStack } from "@chakra-ui/react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import PortfolioBreakdown from "./components/Portfolio/PortfolioBreakdown";

function App() {
  return (
    <>
      <VStack minHeight={"100vh"}>
        <Navbar />
        <BrowserRouter basename="/">
          <Routes>
            <Route path="/" element={<FinancialForm />} />
            <Route path="/custom-portfolio" element={<PortfolioBreakdown />} />
          </Routes>
        </BrowserRouter>
      </VStack>
      <Footer />
    </>
  );
}

export default App;
