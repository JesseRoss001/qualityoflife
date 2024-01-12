import React from 'react';
import React, { useRef, useState } from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls } from '@react-three/drei';

function CountryComparison() {
  // Your component logic here

  return (
    <div>
      <h2>Compare Countries</h2>
      <Canvas>
        {/* Your 3D objects will go here */}
        <OrbitControls />
      </Canvas>
    </div>
  );
}

export default CountryComparison;