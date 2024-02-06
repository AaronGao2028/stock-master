import { VStack } from "@chakra-ui/react";
import PortfolioList from "./PortfolioList";
import StockDistributionPieChart from "./StockDistributionPieChart";
import PortfolioHeatMap from "./PortfolioHeatMap";
import SectorAllocationPieChart from "./SectorAllocationPieChart";
import HistoricalPerformanceChart from "./HistoricalPerformanceChart";

const PortfolioBreakdown = () => {
  return (
    <VStack>
      <PortfolioList />
      <PortfolioHeatMap />
      <SectorAllocationPieChart />
      <HistoricalPerformanceChart />
    </VStack>
  );
};

export default PortfolioBreakdown;
