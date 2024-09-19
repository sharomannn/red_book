import axios from "axios";

const csrfHeader = { "X-CSRFToken": localStorage.getItem("token") };

const setToken = (newToken: string) => {
  const preparedToken = newToken ? `Token ${newToken}` : "";
  axios.defaults.headers.common["Authorization"] = preparedToken;
  newToken ? localStorage.setItem("token", newToken) : clearToken();
};

const clearToken = () => {
  localStorage.removeItem("token");
};

const apiBaseURL = import.meta.env.VITE_BASE_URL;

axios.defaults.baseURL = apiBaseURL;

axios.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response.status === 401 || error.response.status === 403) {
      clearToken();
    }

    return Promise.reject(error);
  }
);

export default {
  csrfHeader,
  setToken,
};
