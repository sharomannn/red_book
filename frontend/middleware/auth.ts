export default defineNuxtRouteMiddleware((to, from) => {
  return navigateTo("auth-form");
  // isAuthenticated() - это пример метода, проверяющего, аутентифицирован ли пользователь.
  //   if (isAuthenticated() === false) {
  //     return navigateTo("/auth-form");
  //   }
});
