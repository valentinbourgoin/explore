import axios from "axios";

// @todo : get from env
const API_URL = "http://localhost:8000/api";

class AuthService {
    cleanUpAuthToken = (str) => {
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