import {
  Button,
  FormControl,
  FormHelperText,
  FormLabel,
  Heading,
  SimpleGrid,
  VStack,
} from "@chakra-ui/react";
import Data from "../../data/Data.json";
import { useState } from "react";

const Selection = (
  uri: string,
  preference: string,
  jsonfile: string,
  selections: string[],
  setSelections: (str: string[]) => void
) => {
  const toggleSelection = (selection: string) => {
    {
      selections.includes(selection)
        ? setSelections(selections.filter((s) => s !== selection))
        : setSelections([...selections, selection]);
    }
  };

  return (
    <VStack paddingLeft={10} paddingRight={10}>
      <FormControl as="fieldset">
        <FormLabel textAlign="center" fontSize={30}>
          {preference} Selection
        </FormLabel>
        <SimpleGrid columns={{ sm: 1, md: 4, lg: 5, xl: 6 }} spacing={6}>
          {Data[jsonfile]?.map((selection) => (
            <Button
              backgroundColor={
                selections.includes(selection) ? "#5f727e" : "#edf2f7"
              }
              onClick={() => toggleSelection(selection)}
              fontSize={15}
            >
              {selection}
            </Button>
          ))}
        </SimpleGrid>
        <FormHelperText>
          Select all the {preference}'s you are interested in.
        </FormHelperText>
      </FormControl>
    </VStack>
  );
};

export default Selection;
