import {
  HStack,
  Heading,
  Table,
  TableCaption,
  TableContainer,
  Tbody,
  Tfoot,
  Th,
  Thead,
  Tr,
  VStack,
} from "@chakra-ui/react";
import { useEffect, useState } from "react";
import {
  PieChart,
  Pie,
  Tooltip,
  BarChart,
  XAxis,
  YAxis,
  Legend,
  CartesianGrid,
  Bar,
} from "recharts";
import "chart.js";

const GetCustomizedPortfolio = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/form")
      .then((response) => response.json())
      .then((json) => setData(json))
      .catch((error) => console.error(error));
  }, []);

  const retrieveData = (data: string[]) => {
    let t: string[][] = [];

    for (let i = 0; i < 9; i++) {
      t[i] = []; // Initialize t[i] as an empty array before pushing values
    }
    for (let i = 0; i < data.length / 9; i++) {
      for (let j = 0; j < 9; j++) {
        t[j].push(data[9 * i + j]);
      }
    }

    return t;
  };

  const temp = retrieveData(data);

  const tickers = temp[0];
  const names = temp[1];
  const prices = temp[2]?.map((s) => parseFloat(s));
  const marketcaps = temp[3]?.map((s) => parseFloat(s));
  const dividends = temp[4]?.map((s) => parseFloat(s));
  const sectors = temp[5];
  const deviations = temp[6]?.map((s) => parseFloat(s));
  const sharperatios = temp[7]?.map((s) => parseFloat(s));
  const allocations = temp[8]?.map((s) => parseFloat(s));

  const buildSectorPercentages = () => {
    const sectorPercentages = new Map();
    for (let i = 0; i < sectors.length; i++) {
      if (sectorPercentages.has(sectors[i])) {
        sectorPercentages.set(
          sectors[i],
          sectorPercentages.get(sectors[i]) + allocations[i]
        );
      } else {
        sectorPercentages.set(sectors[i], 0);
      }
    }
    return sectorPercentages;
  };

  const sectorPercentages = buildSectorPercentages();

  const chartData = tickers?.map((ticker, index) => ({
    ticker: ticker,
    percent: Math.round(10000 * allocations[index]) / 100,
  }));

  const sectorPercentageToJson = () => {
    const sectorData: { sector: string; percent: number }[] = [];

    for (const [key, value] of sectorPercentages.entries()) {
      sectorData.push({
        sector: key,
        percent: Math.round(10000 * value) / 100,
      });
    }

    return sectorData;
  };

  const sectorData: { sector: string; percent: number }[] =
    sectorPercentageToJson();

  const categories = [
    "Ticker",
    "Name",
    "Price",
    "Market Cap",
    "Dividend",
    "Sector",
    "Standard Deviation",
    "Sharpe Ratio",
    "Allocation",
  ];

  return (
    <VStack marginTop={100} width={"100vw"}>
      <Heading>Customized Portfolio</Heading>
      <TableContainer>
        <Table variant="simple">
          <Thead>
            <Tr>
              {categories.map((c) => (
                <th fontSize={16}>{c}</th>
              ))}
            </Tr>
          </Thead>
          <Tbody>
            {tickers?.map((ticker, index) => (
              <Tr>
                <Th fontSize={14}>{ticker}</Th>
                <Th fontSize={14}>{names[index]}</Th>
                <Th fontSize={14}>${Math.round(prices[index] * 100) / 100}</Th>
                <Th fontSize={14}>
                  ${Math.round(marketcaps[index] * 100) / 100}
                </Th>
                <Th fontSize={14}>
                  ${Math.round(dividends[index] * 100) / 100}
                </Th>
                <Th fontSize={14}>{sectors[index]}</Th>
                <Th fontSize={14}>
                  ${Math.round(deviations[index] * 100) / 100}
                </Th>
                <Th fontSize={14}>
                  ${Math.round(sharperatios[index] * 100) / 100}
                </Th>
                <Th fontSize={14}>
                  {Math.round(allocations[index] * 10000) / 100}%
                </Th>
              </Tr>
            ))}
          </Tbody>
        </Table>
      </TableContainer>
      <Heading marginTop={100}>Charts</Heading>

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

      <Heading>Sector Distribution</Heading>
      <PieChart width={1000} height={600}>
        <Pie
          dataKey="percent"
          isAnimationActive={true}
          data={sectorData}
          outerRadius={250}
          fill="#8884d8"
        />
        <Tooltip
          formatter={(value, name, props) => {
            const { payload } = props;
            return [`${payload.sector}: ${payload.percent}%`];
          }}
        />
      </PieChart>
    </VStack>
  );
};

export default GetCustomizedPortfolio;
