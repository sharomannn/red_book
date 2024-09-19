import { makeRequest } from "../http";

const baseURL = "/backend";

export function getRedBookEntries(): Promise<T> {
  return makeRequest({
    url: `${baseURL}/red_book_entries/`,
    method: "GET",
  });
}

export function getRedBookEntrie(id: number): Promise<T> {
  return makeRequest({
    url: `${baseURL}/red_book_entries/${id}/`,
    method: "GET",
  });
}

export function createRedBookEntrie(data: unknown) {
  return makeRequest({
    url: `${baseURL}/red_book_entries/`,
    method: "POST",
    data,
  });
}

export function updateRedBookEntrie(id: number, data: unknown) {
  return makeRequest({
    url: `${baseURL}/red_book_entries/${id}/`,
    method: "PATCH",
    data,
  });
}

export function getObservation(params: unknown) {
  return makeRequest({
    url: `${baseURL}/observation/`,
    method: "GET",
    params,
  });
}
