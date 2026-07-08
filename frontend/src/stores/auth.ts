import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import api from '../utils/api'

export const useAuthStore = defineStore('auth', () => {
  const token = ref<string | null>(localStorage.getItem('token'))
  const user = ref<any>(null)
  const isLoading = ref(false)
  const error = ref<string | null>(null)

  const isAuthenticated = computed(() => !!token.value)

  const register = async (fullName: string, email: string, password: string) => {
    isLoading.value = true
    error.value = null
    try {
      const response = await api.post('/auth/register', {
        full_name: fullName,
        email,
        password
      })
      user.value = response.data
      return response.data
    } catch (err: any) {
      error.value = err.response?.data?.detail || 'Registration failed'
      throw err
    } finally {
      isLoading.value = false
    }
  }
// revert code 


//   const login = async (email: string, password: string) => {
//     isLoading.value = true
//     error.value = null
//     try {
//       const formData = new FormData()
//       formData.append('username', email)
//       formData.append('password', password)
      
//       const response = await api.post('/auth/login', formData)
//       token.value = response.data.access_token
//       localStorage.setItem('token', response.data.access_token)
      
//       // Get current user info
//       await getCurrentUser()
//       return response.data
//     } catch (err: any) {
//       error.value = err.response?.data?.detail || 'Login failed'
//       throw err
//     } finally {
//       isLoading.value = false
//     }
//   } ///

const login = async (email: string, password: string) => {
  isLoading.value = true
  error.value = null

  try {
    const params = new URLSearchParams()
    params.append("username", email)
    params.append("password", password)

    const response = await api.post(
      "/auth/login",
      params,
      {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      }
    )

    token.value = response.data.access_token
    localStorage.setItem("token", response.data.access_token)

    await getCurrentUser()

    return response.data

  } catch (err: any) {
    error.value = err.response?.data?.detail || "Login failed"
    throw err
  } finally {
    isLoading.value = false
  }
}

  const getCurrentUser = async () => {
    try {
      const response = await api.get('/auth/me')
      user.value = response.data
    } catch (err: any) {
      console.error('Failed to fetch current user:', err)
    }
  }

  const logout = () => {
    token.value = null
    user.value = null
    localStorage.removeItem('token')
  }

  if (token.value) {
    getCurrentUser()
  }

  return {
    token,
    user,
    isLoading,
    error,
    isAuthenticated,
    register,
    login,
    logout,
    getCurrentUser
  }
})
