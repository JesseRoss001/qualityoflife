import React, { useContext, useState, useEffect, useCallback } from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls } from '@react-three/drei';
import * as d3 from 'd3';

import { DataContext } from '../DataContext'; // Import DataContext from your context file

function CountryComparison() {
  const { data } = useContext(DataContext);

  const [displayTop, setDisplayTop] = useState(true);
  const [filteredData, setFilteredData] = useState([]);

  useEffect(() => {
    // Function to filter and get the relevant data for display
    const getFilteredData = () => {
      const sortedData = [...data].sort((a, b) =>
        displayTop ? a['Final Rank'] - b['Final Rank'] : b['Final Rank'] - a['Final Rank']
      );
      return displayTop ? sortedData.slice(0, 10) : sortedData.slice(-10);
    };

    const filtered = getFilteredData();
    setFilteredData(filtered);
  }, [data, displayTop]);

  const toggleDisplay = () => {
    setDisplayTop(!displayTop);
  };
  // Updated createBarChart function with useCallback
  const createBarChart = useCallback(() => {
    const width = 800;
    const height = 400;
    const margin = { top: 20, right: 20, bottom: 30, left: 40 };

    // Clear previous SVG
    d3.select('#chart-container').selectAll('*').remove();

    // Create SVG container
    const svg = d3.select('#chart-container')
                  .append('svg')
                  .attr('width', width)
                  .attr('height', height);

    // Scales
    const xScale = d3.scaleBand()
                     .range([0, width - margin.left - margin.right])
                     .padding(0.1)
                     .domain(filteredData.map(d => d['Country or region']));
    const yScale = d3.scaleLinear()
                     .range([height - margin.top - margin.bottom, 0])
                     .domain([0, d3.max(filteredData, d => d['Composite Score'])]);

    // Axes
    const xAxis = d3.axisBottom(xScale);
    const yAxis = d3.axisLeft(yScale);

    // Add X axis
    svg.append('g')
       .attr('transform', `translate(${margin.left},${height - margin.bottom})`)
       .call(xAxis);

    // Add Y axis
    svg.append('g')
       .attr('transform', `translate(${margin.left}, ${margin.top})`)
       .call(yAxis);

    // Bars
    svg.selectAll('.bar')
       .data(filteredData)
       .enter().append('rect')
       .attr('class', 'bar')
       .attr('x', d => xScale(d['Country or region']) + margin.left)
       .attr('y', d => yScale(d['Composite Score']) + margin.top)
       .attr('width', xScale.bandwidth())
       .attr('height', d => height - margin.top - margin.bottom - yScale(d['Composite Score']))
       .attr('fill', 'blue');

  }, [filteredData]);

  useEffect(() => {
    createBarChart();
  }, [filteredData, createBarChart]);
  return (
    <div>
      <h2>Compare Countries</h2>
      <button onClick={toggleDisplay}>
        {displayTop ? 'Show Bottom 10' : 'Show Top 10'}
      </button>

      <div id="chart-container"></div> {/* Container for the 3D bar chart */}

      {/* Display the countries on cards */}
      <div className="country-cards">
        {filteredData.map((country, index) => (
          <div key={index} className="country-card">
            <p>{country['Country or region']}</p>
            <p>Composite Score: {country['Composite Score']}</p>
            {/* Include other data fields as needed */}
          </div>
        ))}
      </div>

      <Canvas>
        <OrbitControls />
      </Canvas>
    </div>
  );
}

export default CountryComparison;
