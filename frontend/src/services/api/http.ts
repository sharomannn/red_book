import axios from "axios";
import { tokenInterceptor } from "./interceptors";

const apiBaseURL = import.meta.env.VITE_BASE_URL;

const instance = axios.create({
  baseURL: apiBaseURL,
});

instance.interceptors.request.use(tokenInterceptor);
instance.interceptors.response.use(
  (response) => response,
  (error) => errorInterceptor(error)
);

type ResponseType =
  | "arraybuffer"
  | "blob"
  | "document"
  | "json"
  | "text"
  | "stream";

export function makeRequest<T>({
  url = "/",
  method = "get",
  headers,
  params,
  data,
  responseType = "json",
}: Request): Promise<T> {
  return axios({
    url,
    method,
    responseType,
    headers: { ...headers },
    params,
    data,
    paramsSerializer: { indexes: null },
    withCredentials: false,
  });
}

export default instance;

// const baseHeaders = import.meta.env.DEV ? { ...config.csrfHeader } : {};
