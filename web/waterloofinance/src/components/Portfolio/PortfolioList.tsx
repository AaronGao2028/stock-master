import {
  Heading,
  Table,
  TableContainer,
  Tbody,
  Th,
  Thead,
  Tr,
  VStack,
} from "@chakra-ui/react";
import GetCustomizedPortfolioData from "../../hooks/GetCustomizedPortfolioData";

const PortfolioList = () => {
  const temp = GetCustomizedPortfolioData();

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
  const tickers = temp[0];
  const names = temp[1];
  const prices = temp[2]?.map((s) => parseFloat(s));
  const marketcaps = temp[3]?.map((s) => parseFloat(s));
  const dividends = temp[4]?.map((s) => parseFloat(s));
  const sectors = temp[5];
  const deviations = temp[6]?.map((s) => parseFloat(s));
  const sharperatios = temp[7]?.map((s) => parseFloat(s));
  const allocations = temp[8]?.map((s) => parseFloat(s));

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
                  {Math.round(dividends[index] * 10000) / 100}%
                </Th>
                <Th fontSize={14}>{sectors[index]}</Th>
                <Th fontSize={14}>
                  {Math.round(deviations[index] * 10000) / 100}%
                </Th>
                <Th fontSize={14}>
                  {Math.round(sharperatios[index] * 100) / 100}
                </Th>
                <Th fontSize={14}>
                  {Math.round(allocations[index] * 10000) / 100}%
                </Th>
              </Tr>
            ))}
          </Tbody>
        </Table>
      </TableContainer>
    </VStack>
  );
};

export default PortfolioList;
