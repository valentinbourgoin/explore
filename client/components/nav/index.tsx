import React, { useState } from 'react'

import Link from 'next/link'
import Image from 'next/image'

import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import AccountCircle from '@mui/icons-material/AccountCircle';
import MoreIcon from '@mui/icons-material/MoreVert';

import { 
    Logo
} from './styled'

import logoUrl from '../../public/images/logo.png'

export default function Nav(props) {

    const {
        user 
    } = props
    const [ color, setColor ] = useState()

    React.useEffect(() => {
        const { color } = props
        setColor(color)

        if (props.changeColorOnScroll) {
          window.addEventListener("scroll", headerColorChange);
        }
        return function cleanup() {
          if (props.changeColorOnScroll) {
            window.removeEventListener("scroll", headerColorChange);
          }
        };
    }, [])

    const headerColorChange = () => {
        const { color, changeColorOnScroll } = props;
        const windowsScrollTop = window.pageYOffset;
        if (windowsScrollTop > changeColorOnScroll.height) {
            setColor(changeColorOnScroll.color)
        } else {
            setColor(color)
        }
    };

    const isTransparent = () => {
        return color === "transparent"
    }

  return (
    <Box sx={{ flexGrow: 1, backgroundColor: (!isTransparent()) ? "white" : null }}>
      <AppBar 
        position="fixed"
        color={(!isTransparent()) ? "inherit" : "transparent"}
        elevation={(isTransparent()) ? 0 : 3}
        >
        <Toolbar>
          <Box sx={{ mr: 2 }}>
            <Link href="/">
                <Logo>
                    <Image
                        src={logoUrl}
                        alt="Explore"
                    />
                </Logo>
            </Link> 
          </Box>
          <Box sx={{ flexGrow: 1 }} />
          { user && 
            <React.Fragment>
                <Box sx={{ display: { xs: 'none', md: 'flex', color:(!isTransparent()) ? "white" : null } }}>
                    <IconButton
                    size="large"
                    edge="end"
                    color="inherit"
                    >
                    <AccountCircle color="inherit" />
                    </IconButton>
                </Box>
                <Box sx={{ display: { xs: 'flex', md: 'none' } }}>
                    <IconButton
                    size="large"
                    color="inherit"
                    >
                    <MoreIcon />
                    </IconButton>
                </Box>
            </React.Fragment>
          }
          { !user && 
            <Link href="/login">
                <Button color="primary" variant="contained">Login</Button>
            </Link>
          }
        </Toolbar>
      </AppBar>
    </Box>
  );
}