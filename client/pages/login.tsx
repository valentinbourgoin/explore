import type { NextPage } from 'next'

import styled from 'styled-components'
import Container from '@material-ui/core/Container'
import Button from '@material-ui/core/Button';

const Login: NextPage = () => {
    const handleStravaAuth = () => {
        if (window) {
            const clientId = 3032;
            const redirectUrl = "http://localhost:3000/redirect";
            const scope = ['activity:read_all'];
            window.location.replace(`http://www.strava.com/oauth/authorize?client_id=${clientId}&response_type=code&redirect_uri=${redirectUrl}/exchange_token&approval_prompt=force&scope=${scope}`);
        }
    }

    return (
        <LoginWrapper img="/images/banner.jpeg">
            <Container maxWidth="sm">
                <LoginForm>
                <h2>Se connecter</h2>
                <p>Lorem ipsum dolor</p>
                <ul>
                    <li>
                        <Button
                            variant="contained" 
                            style={{background: "rgb(252, 42, 0)", color: "white"}}
                            onClick={() => { handleStravaAuth() }}
                        >
                            Se connecter avec Strava
                        </Button>
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