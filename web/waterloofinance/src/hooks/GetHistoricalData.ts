import React, { useEffect, useState } from "react";

const GetHistoricalData = (ticker: string) => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://localhost:5000/historical?ticker="+ticker);
        const json = await response.json();
        setData(json);
      } catch (error) {
        console.error(error);
      }
    };

    fetchData();
  }, []);

  return data;
}

export default GetHistoricalData;
