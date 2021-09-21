// import React from 'react'
// import Image from 'next/image'
// import Link from 'next/link'

// import Button from '@material-ui/core/Button';

// import { 
//     Container,
//     Logo
// } from './styled'

// import logo from '../../public/images/logo.png'

// const Nav:React.FC = () => {
//     return (
//         <>
//         <Container>
//             <Logo>
//                 <Link href="/">
//                     <Image
//                         src={logo}
//                         alt="Explore"
//                     />
//                 </Link>
//             </Logo>
//             <Link href="/login">
//                 <Button variant="contained" color="primary">
//                     Login
//                 </Button>
//             </Link>
//         </Container>
//         </>
//     )
// }

// export default Nav

import React from 'react'

import Link from 'next/link'
import Image from 'next/image'

import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import AccountCircle from '@mui/icons-material/AccountCircle';
import MoreIcon from '@mui/icons-material/MoreVert';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/icons-material/Menu';

// import MenuIcon from '@mui/icons-material/Menu';

import { 
    Logo
} from './styled'

import logoUrl from '../../public/images/logo.png'

export default function Nav(props) {

    const { user } = props

  return (
    <Box sx={{ flexGrow: 1, backgroundColor: "white" }}>
      <AppBar 
        position="fixed"
        color="inherit"
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
                <Box sx={{ display: { xs: 'none', md: 'flex' } }}>
                    <IconButton
                    size="large"
                    edge="end"
                    color="inherit"
                    >
                    <AccountCircle />
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