import React from 'react'
import Image from 'next/image'
import Link from 'next/link'

import Button from '@material-ui/core/Button';

import { 
    Container,
    Logo
} from './styled'

import logo from '../../public/images/logo.png'

const Nav:React.FC = () => {
    return (
        <>
        <Container>
            <Logo>
                <Link href="/">
                    <Image
                        src={logo}
                        alt="Explore"
                    />
                </Link>
            </Logo>
            <Link href="/login">
                <Button variant="contained" color="primary">
                    Login
                </Button>
            </Link>
        </Container>
        </>
    )
}

export default Nav