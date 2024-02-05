import { Heading } from "@chakra-ui/react";
import { PieChart, Pie, Tooltip } from "recharts";
import GetCustomizedPortfolioData from "../../hooks/GetCustomizedPortfolioData";

const StockDistributionPieChart = () => {
  const temp = GetCustomizedPortfolioData();

  const tickers = temp[0];
  const names = temp[1];
  const prices = temp[2]?.map((s) => parseFloat(s));
  const marketcaps = temp[3]?.map((s) => parseFloat(s));
  const dividends = temp[4]?.map((s) => parseFloat(s));
  const sectors = temp[5];
  const deviations = temp[6]?.map((s) => parseFloat(s));
  const sharperatios = temp[7]?.map((s) => parseFloat(s));
  const allocations = temp[8]?.map((s) => parseFloat(s));

  const chartData = tickers?.map((ticker, index) => ({
    ticker: ticker,
    percent: Math.round(10000 * allocations[index]) / 100,
  }));

  return (
    <>
      <Heading>Stock Distribution</Heading>
      <PieChart width={1000} height={600}>
        <Pie
          dataKey="percent"
          isAnimationActive={true}
          data={chartData}
          outerRadius={250}
          fill="#8884d8"
        />
        <Tooltip
          formatter={(value, name, props) => {
            const { payload } = props;
            return [`${payload.ticker}: ${payload.percent}%`];
          }}
        />
      </PieChart>
    </>
  );
};

export default StockDistributionPieChart;
