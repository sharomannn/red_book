import request from "./request";

export const getAnimals = (params?: {}) =>
  request({
    url: "red_book_entries",
    method: "GET",
    params,
  });


export const detailAnimal = (id) => 
  request({
    url: `red_book_entries/${id}`,
    method: "GET",
  })