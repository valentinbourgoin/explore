import React, { useState, useEffect } from 'react';
import type { NextPage } from 'next'
import Link from 'next/link'

import GridService from '../services/grid'

import styled from 'styled-components'
import Container from '@material-ui/core/Container'

const Dashboard: NextPage = () => {
  const [grids, setGrids] = useState([]);
 
  useEffect(() => {
    const fetchData = async () => {
      const result = await GridService.getGrids()
      setGrids(result);
    };

    fetchData();
  }, []);


  return (
    <>
      <Container maxWidth="sm">
        <h1>Dashboard</h1>
        <p>LaLALLALA</p>
        <p>LAL</p>
        <p>LAL</p>
        <ul>
        {grids.map((item, i) => (
          <li key={i}>
            <Link href={`/grid/${item.id}`}>
              {item.name}
            </Link>
          </li>
        ))}
        </ul>
      </Container>
    </>
  )

}

export default Dashboard
