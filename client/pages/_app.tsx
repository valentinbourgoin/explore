import type { AppProps } from 'next/app'
import { ThemeProvider } from '@material-ui/core/styles';

import styled from 'styled-components'

import theme from '../theme/theme'
import GlobalStyle from '../theme/global'

import Nav from '../components/nav'

function Explore({ Component, pageProps }: AppProps) {
  return (
    <ThemeProvider theme={theme}>
      <GlobalStyle />
      <Nav user={{}} />
      <Wrapper>
        <Component {...pageProps} />
      </Wrapper>
    </ThemeProvider>
  )
}

const Wrapper = styled.div`
  position: relative;
  top: 4rem;
`

export default Explore
