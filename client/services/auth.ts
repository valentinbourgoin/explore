import axios from "axios";

const API_URL = process.env.NEXT_PUBLIC_API_URL

class AuthService {
    cleanUpAuthToken = (str: string) => {
        return str.split("&")[1].slice(5);
    };

    getTokenByCode = async (code: string, provider='strava') => {
        try {
            let result = await axios.post(
                `${API_URL}/rest-auth/${provider}/`,
                { code }
            ) 
            return result.data.key
        } catch (e) {
          console.log('BAD AUTHENT')
          console.log(e)
          return false;
        }
    }

    storeToken = (token: string) => {
        localStorage.setItem('token', token)
    }

    getToken = () => {
        return localStorage.getItem('token')
    }

    getAuthHeaders = () => {
        const token = this.getToken()
        if (token) {
            return { Authorization: `Token ${token}` };
        } else {
            return {};
        }
    }
}

export default new AuthService();