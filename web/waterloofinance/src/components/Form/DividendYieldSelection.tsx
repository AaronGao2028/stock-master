import Selection from "./Selection";

interface Props {
  selections: string[];
  setSelections: (str: string[]) => void;
}

const DividendYieldSelection = ({ selections, setSelections }: Props) =>
  Selection(
    "dividend_preferences",
    "Dividend",
    "dividends",
    selections,
    setSelections
  );

export default DividendYieldSelection;
