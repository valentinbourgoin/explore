import type { AppProps } from 'next/app'
import { ThemeProvider } from '@material-ui/core/styles';

import theme from '../theme/theme'
import GlobalStyle from '../theme/global'

function Explore({ Component, pageProps }: AppProps) {
  return (
    <ThemeProvider theme={theme}>
      <GlobalStyle />
      <Component {...pageProps} />
    </ThemeProvider>
  )
}

export default Explore
