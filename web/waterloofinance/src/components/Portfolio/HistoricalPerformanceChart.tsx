import GetHistoricalData from "../../hooks/GetHistoricalData";

const HistoricalPerformanceChart = () => {
  const temp = GetHistoricalData("AAPL");
  const dates = [];
  const prices = [];

  const fetchData = () => {};
  return <div>{temp}</div>;
};

export default HistoricalPerformanceChart;
