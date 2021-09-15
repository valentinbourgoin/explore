import type { AppProps } from 'next/app'
import { ThemeProvider } from '@material-ui/core/styles';

import theme from '../theme/theme'
import GlobalStyle from '../theme/global'

import Nav from '../components/nav'

function Explore({ Component, pageProps }: AppProps) {
  return (
    <ThemeProvider theme={theme}>
      <GlobalStyle />
      <Nav />
      <Component {...pageProps} />
    </ThemeProvider>
  )
}
export default Explore
