import {
  Stack,
  Slider,
  SliderTrack,
  SliderFilledTrack,
  SliderThumb,
  Tooltip,
  SliderMark,
  Heading,
} from "@chakra-ui/react";
import { useState } from "react";

interface Props {
  sliderValue: number;
  setSliderValue: (num: number) => void;
}

const PortfolioSlider = ({ sliderValue, setSliderValue }: Props) => {
  return (
    <>
      <Heading>Number of Stocks in Portfolio</Heading>
      <Heading>{sliderValue}</Heading>
      <Slider
        marginTop={10}
        id="slider"
        defaultValue={100}
        min={10}
        max={200}
        colorScheme="teal"
        onChange={(v) => setSliderValue(v)}
        width="70vw"
      >
        <SliderMark value={50} mt="1" ml="-2.5" fontSize="sm">
          50
        </SliderMark>
        <SliderMark value={100} mt="1" ml="-2.5" fontSize="sm">
          100
        </SliderMark>
        <SliderMark value={150} mt="1" ml="-2.5" fontSize="sm">
          150
        </SliderMark>
        <SliderTrack>
          <SliderFilledTrack />
        </SliderTrack>
        <Tooltip hasArrow bg="teal.500" color="white" placement="top">
          <SliderThumb />
        </Tooltip>
      </Slider>
    </>
  );
};

export default PortfolioSlider;
