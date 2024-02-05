import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { color } from "chart.js/helpers";
import { TreemapController, TreemapElement } from "chartjs-chart-treemap";
import { Chart } from "react-chartjs-2";
import GetCustomizedPortfolioData from "../../hooks/GetCustomizedPortfolioData";
import { Heading, VStack } from "@chakra-ui/react";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
  TreemapController,
  TreemapElement
);

const PortfolioHeatMap = () => {
  const temp = GetCustomizedPortfolioData();

  const tickers = temp[0];
  const sharperatios = temp[7]?.map((s) => parseFloat(s));
  const allocations = temp[8]?.map((s) => parseFloat(s));

  const data = tickers?.map((ticker, index) => ({
    name: ticker.toUpperCase(),
    allocation: Math.round(10000 * allocations[index]) / 100,
    sharperatio: Math.round(100 * sharperatios[index]) / 100,
  }));

  const options = {
    plugins: {
      legend: {
        display: false,
      },
      tooltip: {
        displayColors: false,
        callbacks: {
          title(items) {
            return items[0].raw._data.name;
          },
          label(item) {
            const {
              _data: { allocation, sharperatio },
            } = item.raw;
            return [
              `Allocation: ${allocation}%`,
              `Sharpe Ratio: ${sharperatio}`,
            ];
          },
        },
      },
    },
  };

  const config = {
    type: "treemap",
    data: {
      datasets: [
        {
          tree: data,
          key: "allocation",
          labels: {
            display: true,
            formatter: (context) => context.raw._data.name,
          },
          backgroundColor(context) {
            if (context.type !== "data") return "transparent";
            const { sharperatio } = context.raw._data;
            return sharperatio === 0
              ? color("grey").rgbString()
              : color("green")
                  .alpha(sharperatio / 2)
                  .rgbString();
          },
        },
      ],
    },
  };

  return (
    <VStack width="90vw">
      <Heading>Portfolio Heat Map</Heading>
      <Chart type="treemap" data={config.data} options={options} />
    </VStack>
  );
};

export default PortfolioHeatMap;
