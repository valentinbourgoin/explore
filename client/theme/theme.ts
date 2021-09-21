import { createTheme } from '@material-ui/core/styles';

// Default theme
// export default {
//     colors: {
//         primary: "#E6B91E",
//         accent: "#B6490D",
//         default: "#1B180E"
//     },
// };

// MaterialUI theme
export default createTheme({
  palette: {
    common: {
        black: "#1B180E",
        white: "#fff"
    },
    primary: {
      main: "#E6B91E",
      light: "#f3de91",
      dark: "#ae8d13",
    },
    secondary: {
      main: "#B6490D",
      light: "#f7b28d", 
      dark: "#772f08",
    },
  },
  components: {
    
  }
});
