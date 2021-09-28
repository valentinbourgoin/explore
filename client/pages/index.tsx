import React, { useEffect, useRef } from 'react';
import type { NextPage } from 'next'
import Head from 'next/head'
import Image from 'next/image'

import styled from 'styled-components'

import Nav from '../components/nav'

import logoSmall from '../public/images/logo-small.png'

const Home: NextPage = () => {

  // Play video
  const video = useRef();
  useEffect(() => {
      setTimeout(() => {
          video.current.play()
      }, 1000)
  }, []);

  return (
    <div>
      <Head>
        <title>Explore</title>
      </Head>

      <Nav 
        color="transparent"
        changeColorOnScroll={{
          height: 200,
          color: "white",
        }}
      />

      <FullContainer>
        <video ref={video} 
          autoPlay 
          loop>
          <source src="https://assets-product.sportheroesgroup.com/communities-running/static/videos/running.webm" type="video/webm" />
          <source src="https://assets-product.sportheroesgroup.com/communities-running/static/videos/running.mp4" type="video/mp4" />
        </video>
        <BaseLine>
          <Image 
            src={logoSmall}
          />
          <h1>Sortez des sentiers battus</h1>
          <h2>Courrez, pédalez, marchez, nagez, partez à l'aventure. Courrez, pédalez, marchez, nagez, partez à l'aventure.</h2>
        </BaseLine>
        <p>Lorem ispsum</p>
        <p>Lorem ispsum</p>
        <p>Lorem ispsum</p>
        <p>Lorem ispsum</p>
        <p>Lorem ispsum</p>
        <p>Lorem ispsum</p>
        <p>Lorem ispsum</p>
        <p>Lorem ispsum</p>
        <p>Lorem ispsum</p>
        <p>Lorem ispsum</p>
        <p>Lorem ispsum</p>
        <p>Lorem ispsum</p>
        <p>Lorem ispsum</p>
        <p>Lorem ispsum</p>
        <p>Lorem ispsum</p>
        <p>Lorem ispsum</p>
        <p>Lorem ispsum</p>
        <p>Lorem ispsum</p>
        <p>Lorem ispsum</p>
        <p>Lorem ispsum</p>
        <p>Lorem ispsum</p>
        <p>Lorem ispsum</p>
        <p>Lorem ispsum</p>
        <p>Lorem ispsum</p>
        <p>Lorem ispsum</p>
        <p>Lorem ispsum</p>
        <p>Lorem ispsum</p>
        <p>Lorem ispsum</p>
      </FullContainer>
    </div>
  )

}

const FullContainer = styled.div`
  width: 100%;
  height: 100vh;
  z-index: 2;
  position: relative;

  video {
    postition: absolute;
    top: 0;
    height: 100%;
    width: 100%;
    object-fit: cover;
    background-size: cover;
  }
`

const BaseLine = styled.div`
  position: absolute;
  top: 10rem; 
  text-align: center;
  color: white; 
  width: 100%;

  img {
    width: 5rem;
  }
  h1, h2 {
    width: 70%;
    margin: 3rem auto;
    line-height: 1.4em;
  }
  h1 {
    font-size: 3em;
  }
  h2 {
    font-size: 1.3em;
  }
`

export default Home
