import { VStack } from "@chakra-ui/react";
import PortfolioList from "./PortfolioList";
import StockDistributionPieChart from "./StockDistributionPieChart";
import PortfolioHeatMap from "./PortfolioHeatMap";
import SectorAllocationPieChart from "./SectorAllocationPieChart";

const PortfolioBreakdown = () => {
  return (
    <VStack>
      <PortfolioList />
      <PortfolioHeatMap />
      <SectorAllocationPieChart />
    </VStack>
  );
};

export default PortfolioBreakdown;
