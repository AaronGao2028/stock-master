import React, { Component } from "react";
import ReactEChartsCore from "echarts-for-react/lib/core";
import * as echarts from "echarts/core";
import { PieChart, PieSeriesOption } from "echarts/charts";
import {
  GridComponent,
  LegendComponent,
  TooltipComponent,
  TitleComponent,
  DatasetComponent,
} from "echarts/components";
import { CanvasRenderer } from "echarts/renderers";
import GetCustomizedPortfolioData from "../../hooks/GetCustomizedPortfolioData";
import { Heading } from "@chakra-ui/react";

echarts.use([
  TitleComponent,
  TooltipComponent,
  GridComponent,
  LegendComponent,
  PieChart,
  CanvasRenderer,
]);

const SectorAllocationPieChart = () => {
  const temp = GetCustomizedPortfolioData();

  const sectors = temp[5];
  const allocations = temp[8]?.map((s) => parseFloat(s));

  const buildSectorPercentages = () => {
    const sectorPercentages = new Map();
    for (let i = 0; i < sectors.length; i++) {
      if (sectorPercentages.has(sectors[i])) {
        sectorPercentages.set(
          sectors[i],
          sectorPercentages.get(sectors[i]) + allocations[i]
        );
      } else {
        sectorPercentages.set(sectors[i], 0);
      }
    }
    return sectorPercentages;
  };

  const sectorPercentages = buildSectorPercentages();

  const sectorPercentageToJson = () => {
    const sectorData: { name: string; value: number }[] = [];

    for (const [key, value] of sectorPercentages.entries()) {
      sectorData.push({
        name: key,
        value: Math.round(10000 * value) / 100,
      });
    }

    return sectorData;
  };

  const sectorData: { name: string; value: number }[] =
    sectorPercentageToJson();

  const data = sectorData;

  const option = {
    series: [
      {
        type: "pie",
        radius: [150, 75],
        center: ["50%", "50%"],
        itemStyle: {
          borderColor: "#fff",
          borderWidth: 1,
        },
        label: {
          alignTo: "edge",
          formatter: "{name|{b}}\n{time|{c}}",
          minMargin: 5,
          edgeDistance: 10,
          lineHeight: 15,
          rich: {
            time: {
              fontSize: 10,
              color: "black",
            },
          },
        },
        labelLine: {
          length: 15,
          length2: 0,
          maxSurfaceAngle: 80,
        },
        labelLayout: function (params) {
          const points = params.labelLinePoints;
          // Update the end point.
          points[2][0] = params.labelRect.x + params.labelRect.width;
          return {
            labelLinePoints: points,
          };
        },
        data: data,
      },
    ],
  };

  return (
    <div style={{ width: "70%", height: "100%" }}>
      <Heading>Sector Allocation</Heading>
      <ReactEChartsCore
        echarts={echarts}
        option={option}
        notMerge={true}
        lazyUpdate={true}
        opts={{}}
        theme={"theme_name"}
      />
    </div>
  );
};

export default SectorAllocationPieChart;
