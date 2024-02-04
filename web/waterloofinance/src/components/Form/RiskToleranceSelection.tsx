import Selection from "./Selection";

interface Props {
  selections: string[];
  setSelections: (str: string[]) => void;
}

const RiskTolerationSelection = ({ selections, setSelections }: Props) =>
  Selection(
    "risk_tolerance",
    "Risk Tolerance",
    "risklevels",
    selections,
    setSelections
  );

export default RiskTolerationSelection;
