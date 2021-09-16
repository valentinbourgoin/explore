import React, { useEffect } from 'react'
import type { NextPage } from 'next'
import { useRouter } from 'next/router'

import AuthService from '../../services/auth'
import UserService from '../../services/user'

const Redirect: NextPage = () => {
  const router = useRouter()

  useEffect(async () => {
    if (location && location.search) {
      const code = AuthService.cleanUpAuthToken(location.search)
      const token = await AuthService.getTokenByCode(code)
      if (token) {
        AuthService.storeToken(token)
        const user = await UserService.getCurrentUser()    
      }
    }
    router.push('/')
  }, []);

  return (
    <div>Loading...</div>
  )

}

export default Redirect