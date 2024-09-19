import axios from "axios";
import { tokenInterceptor } from "./interceptors";

const apiBaseURL = import.meta.env.VITE_BASE_URL;

const instance = axios.create({
  baseURL: apiBaseURL,
});

instance.interceptors.request.use(tokenInterceptor);
instance.interceptors.response.use((response) => response);

export default instance;
