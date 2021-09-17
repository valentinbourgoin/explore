import React from 'react'
import Button from '@material-ui/core/Button';

const CLIENT_URL = process.env.NEXT_PUBLIC_CLIENT_URL
const STRAVA_CLIENT_ID = process.env.NEXT_PUBLIC_STRAVA_CLIENT_ID
const STRAVA_SCOPE = process.env.NEXT_PUBLIC_STRAVA_SCOPE

const StravaAuth:React.FC = () => {
    const handleStravaAuth = () => {
        if (window) {
            const clientId = STRAVA_CLIENT_ID;
            const redirectUrl = `${CLIENT_URL}/redirect`;
            const scope = STRAVA_SCOPE;
            window.location.replace(`http://www.strava.com/oauth/authorize?client_id=${clientId}&response_type=code&redirect_uri=${redirectUrl}/exchange_token&approval_prompt=force&scope=${scope}`);
        }
    }

    return (
        <>
            <Button
                variant="contained" 
                style={{background: "rgb(252, 42, 0)", color: "white"}}
                onClick={() => { handleStravaAuth() }}
            >
                Se connecter avec Strava
            </Button>
        </>
    )
}

export default StravaAuth