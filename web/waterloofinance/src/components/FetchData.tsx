import { useEffect, useState } from "react";

const FetchData = () => {
  const [data, setData] = useState([{}]);

  useEffect(() => {
    fetch("http://localhost:5000/stocks")
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        console.log(data);
      });
  }, []);

  return (
    <div>
      {data.map((stock) => (
        <p>{JSON.stringify(stock)}</p>
      ))}
    </div>
  );
};

export default FetchData;
