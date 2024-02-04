import Selection from "./Selection";

interface Props {
  selections: string[];
  setSelections: (str: string[]) => void;
}

const ShareTurnOver = ({ selections, setSelections }: Props) =>
  Selection(
    "shareturnover_preferences",
    "Share Turnover",
    "shareturnovers",
    selections,
    setSelections
  );

export default ShareTurnOver;
