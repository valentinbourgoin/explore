import type { NextPage } from 'next'

import styled from 'styled-components'
import Container from '@material-ui/core/Container'

import StravaAuth from '../components/strava-auth'

const Login: NextPage = () => {
    return (
        <LoginWrapper img="/images/banner.jpeg">
            <Container maxWidth="sm">
                <LoginForm>
                <h2>Se connecter</h2>
                <p>Lorem ipsum dolor</p>
                <ul>
                    <li>
                        <StravaAuth />
                    </li>
                </ul>
                </LoginForm>
            </Container>
        </LoginWrapper>
    )
}

const LoginWrapper = styled.div`
    width: 100%;
    height: 100vh;
    background: url(${props => props.img}) center;
    background-position: cover;
    display: flex;
    align-items: center;
    justify-content: center;
`

const LoginForm = styled.div`
    width: 100%;
    background: white;
    text-align: center;
    padding: 3rem;

    h2 {

    }

    p {
        margin: 2rem 0;
    }

    ul {
        list-style: none;
    }
`

export default Login