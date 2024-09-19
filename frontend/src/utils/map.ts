// ссылка на карту вне модуля,
let mapWindow: Window | null = null;

/** Закрытие карты. Если есть ссылаа на вкладку, то закрываем её, обнуляем переменную и отписываемся от события закрытия вкладки/браузера */
function close() {
  if (mapWindow) mapWindow?.close();
  mapWindow = null;
  unsubscribeCloseMap();
}

export function useMap() {
  /** При вызове открытия, предварительно закрываем всё что было открыто ранее, запоминаем новую ссылку и подписываемся на события отписки */
  const open = () => {
    close();
    mapWindow = window.open("/map/animals", "_blank");
    subscribeCloseMap();
  };

  const subscribers: { [key: string]: Function[] } = {};

  function on<T>(type: string, callback: (args: T) => void) {
    if (typeof callback !== "function")
      return console.warn("Не удалось опеделить функцию для вызова");
    if (!subscribers[type]) subscribers[type] = [callback];
    else subscribers[type].push(callback);
  }

  const emitter = (event: MessageEvent) => {
    const { type, message } = event.data;
    if (subscribers[type])
      subscribers[type].forEach((fn) => fn(JSON.parse(message)));
  };

  // если где-то ещё использовать этот хук, то не открывать по новой и не вешать обсёрвер
  if (
    !mapWindow &&
    window.location.pathname !== "/map/animals" &&
    !import.meta.env.DEV
  )
    open();

  // можно протипизировать сообщения формата { type: 'type', data: {data} }
  const send = <T>(type: string, message: T) => {
    if (!mapWindow)
      return console.warn("Не удалось найти ссылку на вкладку карты");

    const newMessage = JSON.stringify(message);
    mapWindow.postMessage({
      type,
      message: newMessage,
    });
  };

  window.addEventListener("message", emitter);

  onBeforeUnmount(() => {
    window.removeEventListener("message", emitter);
  });

  return {
    send,
    open,
    close,
    on,
  };
}

function unsubscribeCloseMap() {
  window.removeEventListener("beforeunload", close);
}

function subscribeCloseMap() {
  window.addEventListener("beforeunload", close);
}
