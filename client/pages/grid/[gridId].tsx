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
  const [grid, setGrid] = useState();
  const [tiles, setTiles] = useState();

  const { gridId } = router.query
  
  useEffect(() => {
    const fetchGrid = async () => {
      const gridDetails = await GridService.getGridDetails(gridId)
      setGrid(gridDetails);
    };

    const fetchTiles = async () => {
      const tiles = await GridService.getGridTiles(gridId)
      setTiles(tiles)
    }

    if (gridId) {
      fetchGrid();
      fetchTiles();
    }
  }, [ gridId ]);


  return (
    <>
    { grid && tiles && 
      <React.Fragment>
        <MapInfos>
          <h1>{grid.name}</h1>
        </MapInfos>
        <MapWrapper>
            <Map grid={grid} tiles={tiles} />
        </MapWrapper>
      </React.Fragment>
    }
    </>
  )

}

const MapInfos = styled.div`
  position: absolute;
  background: white;
  padding: 3rem;
  right: 0; 
  top: 0;
  z-index: 1000;
`

const MapWrapper = styled.div`
  height: calc(100vh - 5rem);
  width: 100%;

  .leaflet-container {
    height: 100%;
  }
`

export default Grid
