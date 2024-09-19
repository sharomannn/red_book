import axios from "axios";
import { tokenInterceptor } from "./interceptors";
interface Request {
  url: string;
  method?: string;
  responseType?: ResponseType;
  headers?: any;
  params?: any;
  data?: any;
  paramsSerializer?: (params: object | string) => string;
}

const mapUrl = {
  local: `${import.meta.env.VITE_APP_API_URL}`,
  prod: `${window.location.origin}/backend`,
};
const apiBaseURL =
  window.location.hostname === "localhost" ? mapUrl.local : mapUrl.prod;

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
    headers: { ...baseHeaders, ...headers },
    params,
    data,
    paramsSerializer: { indexes: null },
    withCredentials: false,
  });
}

export default instance

const baseHeaders = import.meta.env.DEV ? { ...config.csrfHeader } : {};
