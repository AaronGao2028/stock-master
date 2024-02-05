import { useEffect, useState } from "react";
import FinancialForm from "./components/Form/FinancialForm";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import { HStack, VStack } from "@chakra-ui/react";
import GetCustomizedPortfolio from "./hooks/GetCustomizedPortfolio";
import PieChartReact from "./hooks/PieChartReact";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import PortfolioList from "./components/Portfolio/PortfolioList";
import PortfolioBreakdown from "./components/Portfolio/PortfolioBreakdown";
import ApexChart from "./components/Portfolio/PortfolioHeatMap";
import TreemapChart from "./components/Portfolio/PortfolioHeatMap";
import PortfolioPieChart from "./components/Portfolio/SectorAllocationPieChart";

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
