import { createGlobalStyle } from 'styled-components'

const GlobalStyle = createGlobalStyle`
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html{
  box-sizing: border-box;
  background: #F5F4F0;
  display:block;
  height: 100%;
  width: 100%;
}

body{
  background-color:#fafafa;
  min-height:100vh;
  font-family:Lato;
}
`;

export default GlobalStyle;