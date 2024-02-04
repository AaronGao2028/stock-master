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
  VStack,
} from "@chakra-ui/react";
import Data from "../data/Data.json";
import { useState } from "react";
import SectorSelection from "./SectorSelection";
import MarketCapSelection from "./MarketCapSelection";
import DividendYieldSelection from "./DividendYieldSelection";
import ShareTurnOver from "./ShareTurnoverSelection";

const FinancialForm = () => {
  return (
    <VStack marginTop={10}>
      <Heading>Stock Master</Heading>
      <SectorSelection />
      <MarketCapSelection />
      <DividendYieldSelection />
      <ShareTurnOver />
    </VStack>
  );
};

export default FinancialForm;
