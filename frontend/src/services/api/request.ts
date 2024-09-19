import axios from "axios";
import config from "./config";
import type { AxiosRequestConfig } from "axios";

const baseHeaders = {
  ...config.csrfHeader,
};

const request = ({
  url = "/",
  method = "get",
  responseType = "json",
  headers,
  params,
  data,
}: AxiosRequestConfig) =>
  axios({
    url,
    method,
    responseType,
    headers: { ...baseHeaders, ...headers },
    params,
    data,
  });

export default request;
