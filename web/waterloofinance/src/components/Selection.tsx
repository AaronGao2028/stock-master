import {
  Button,
  FormControl,
  FormHelperText,
  FormLabel,
  Heading,
  SimpleGrid,
  VStack,
} from "@chakra-ui/react";
import Data from "../data/Data.json";
import { useState } from "react";

const Selection = (uri: string, preference: string, jsonfile: string) => {
  const [selections, setSelections] = useState([""]);

  const submitSelections = async () => {
    await fetch("http://localhost:5000/" + uri, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(selections),
    });
  };

  const toggleSelection = (selection: string) => {
    {
      selections.includes(selection)
        ? setSelections(selections.filter((s) => s !== selection))
        : setSelections([...selections, selection]);
    }
  };

  return (
    <VStack paddingLeft={10} paddingRight={10} paddingTop={10}>
      <FormControl as="fieldset">
        <FormLabel textAlign="center" fontSize={20}>
          {preference} Selection
        </FormLabel>
        <SimpleGrid columns={{ sm: 1, md: 4, lg: 5, xl: 6 }} spacing={6}>
          {Data[jsonfile]?.map((sector) => (
            <Button
              backgroundColor={
                selections.includes(sector) ? "#5f727e" : "#edf2f7"
              }
              onClick={() => toggleSelection(sector)}
              fontSize={15}
            >
              {sector}
            </Button>
          ))}
        </SimpleGrid>
        <FormHelperText>
          Select all the {preference}'s you are interested in.
        </FormHelperText>
      </FormControl>
      <Button onClick={submitSelections}>Submit</Button>
    </VStack>
  );
};

export default Selection;
