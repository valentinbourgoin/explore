import axios from "axios"
import AuthService from './auth'

const API_URL = process.env.NEXT_PUBLIC_API_URL

class UserService {

    getCurrentUser = async () => {
        if (localStorage.getItem('user')) {
            return JSON.parse(localStorage.getItem('user'))
        } 
        if (localStorage.getItem('token')) {
            try {
                let result = await axios.get(`${API_URL}/users/me/`, { headers: AuthService.getAuthHeaders() }) 
                localStorage.setItem('user', JSON.stringify(result.data))
                return result.data
            } catch(e) {
                console.log(e)
                // localStorage.clear('token')
            }
        }
        return false
    }
}

export default new UserService();