import React, { useEffect, useState } from "react";

const GetCustomizedPortfolioData = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://localhost:5000/form");
        const json = await response.json();
        setData(json);
      } catch (error) {
        console.error(error);
      }
    };

    fetchData();
  }, []);

  const retrieveData = (data: string[]) => {
    let t: string[][] = [];

    for (let i = 0; i < 9; i++) {
      t[i] = [];
    }
    for (let i = 0; i < data.length / 9; i++) {
      for (let j = 0; j < 9; j++) {
        t[j].push(data[9 * i + j]);
      }
    }

    return t;
  };

  const temp = retrieveData(data);
  return temp;
};

export default GetCustomizedPortfolioData;
