import {
  Button,
  FormControl,
  FormHelperText,
  FormLabel,
  HStack,
  Heading,
  Input,
  Radio,
  RadioGroup,
  SimpleGrid,
  Slider,
  VStack,
} from "@chakra-ui/react";
import Data from "../../data/Data.json";
import { useState } from "react";
import SectorSelection from "./SectorSelection";
import MarketCapSelection from "./MarketCapSelection";
import DividendYieldSelection from "./DividendYieldSelection";
import ShareTurnOver from "./ShareTurnoverSelection";
import RiskTolerationSelection from "./RiskToleranceSelection";
import ShareTurnoverSelection from "./ShareTurnoverSelection";
import PortfolioSlider from "./PortfolioSlider";

const FinancialForm = () => {
  const [index, setIndex] = useState(0);
  const [sectors, setSectors] = useState([""]);
  const [marketcaps, setMarketcaps] = useState([""]);
  const [turnovers, setTurnovers] = useState([""]);
  const [dividends, setDividends] = useState([""]);
  const [risks, setRisks] = useState([""]);
  const [sliderValue, setSliderValue] = useState(100);

  const form = [
    <SectorSelection selections={sectors} setSelections={setSectors} />,
    <MarketCapSelection
      selections={marketcaps}
      setSelections={setMarketcaps}
    />,
    <ShareTurnoverSelection
      selections={turnovers}
      setSelections={setTurnovers}
    />,
    <DividendYieldSelection
      selections={dividends}
      setSelections={setDividends}
    />,
    <RiskTolerationSelection selections={risks} setSelections={setRisks} />,
    <PortfolioSlider
      sliderValue={sliderValue}
      setSliderValue={setSliderValue}
    />,
  ];

  const submitForm = async () => {
    await fetch("http://localhost:5000/form", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify([
        sectors,
        marketcaps,
        turnovers,
        dividends,
        risks,
        sliderValue,
      ]),
    });
    window.open("http://127.0.0.1:5173/custom-portfolio");
  };

  return (
    <VStack marginTop={200} width="100vw">
      {form[index]}
      <HStack marginTop={100} spacing="50vw">
        <Button
          display={index === 0 ? "none" : "block"}
          onClick={() => setIndex(index - 1)}
        >
          Previous
        </Button>
        <Button
          display={index === form.length - 1 ? "none" : "block"}
          onClick={() => setIndex(index + 1)}
        >
          Next
        </Button>
        <Button
          display={index === form.length - 1 ? "block" : "none"}
          onClick={submitForm}
        >
          Submit
        </Button>
      </HStack>
    </VStack>
  );
};

export default FinancialForm;
