import styled from 'styled-components'

export const Container = styled.div`
    display: flex;
    justify-content:space-evenly;
    align-items: left;
    color: white;
    background-color: white;
    width: 100%;
    padding: 1rem;
    z-index: 100;
    position: fixed;
    top: 0;
    left: 0;
`

export const Logo = styled.div`
    height: 100%;
    width: 8rem;

    img {
        height: 100%;
        max-width: 8rem;
    }
`