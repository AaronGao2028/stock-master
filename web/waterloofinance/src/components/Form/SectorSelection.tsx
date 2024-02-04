import Selection from "./Selection";

interface Props {
  selections: string[];
  setSelections: (str: string[]) => void;
}

const SectorSelection = ({ selections, setSelections }: Props) =>
  Selection(
    "sector_preferences",
    "Sector",
    "sectors",
    selections,
    setSelections
  );

export default SectorSelection;
