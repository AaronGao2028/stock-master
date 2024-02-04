import Selection from "./Selection";

interface Props {
  selections: string[];
  setSelections: (str: string[]) => void;
}

const SectorSelection = ({ selections, setSelections }: Props) =>
  Selection(
    "marketcap_preferences",
    "Market Cap",
    "marketcaps",
    selections,
    setSelections
  );

export default SectorSelection;
