import React, { useState, useEffect } from 'react';
import type { NextPage } from 'next'
import { useRouter } from 'next/router'
import dynamic from 'next/dynamic'

import GridService from '../../services/grid'

import styled from 'styled-components'
import Container from '@material-ui/core/Container'

const Map = dynamic(
  () => import('../../components/map'),
  { ssr: false }
)

const Grid: NextPage = () => {
  const router = useRouter()
  const [grid, setGrid] = useState([]);

  const { gridId } = router.query
  
  useEffect(() => {
    const fetchData = async () => {
      const result = await GridService.getGridDetails(gridId)
      setGrid(result);
    };

    if (gridId) {
      fetchData();
    }
  }, [ gridId ]);


  return (
    <>
      <Container maxWidth="sm">
        <h1>Grid</h1>
        <p>LaLALLALA</p>
        <p>LAL</p>
        <p>LAL</p>
        <h1>{grid.name}</h1>
        <Map grid={grid} />
      </Container>
    </>
  )

}

export default Grid
